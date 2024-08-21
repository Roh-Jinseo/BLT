from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import os
from django.conf import settings
from .serializers import DepositOptionSerializer,DepositSerializer,SavingSerializer,SavingOptionSerializer
from .serializers import CombinedDepositSerializer,CombinedSavingSerializer
from .models import DepositOptions, DepositProducts,SavingOptions,SavingProducts
from django.db.models import Max
from django.core import serializers
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

# from .models import finlife


'''
여기부터는 예금
'''
# Create your views here.
API_KEY = settings.API_KEY
url_deposit = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
params_deposit = {
    'auth':API_KEY,
    # 금융회사 코드
    'topFinGrpNo': '020000',
    'pageNo':1
}


# def index(request):
#     response = requests.get(url_deposit,params=params_deposit).json()
#     return JsonResponse(response)

    


@api_view(['GET'])
def save_deposit_products(request):
    response = requests.get(url_deposit, params=params_deposit).json()

    # 상품목록
    if len(DepositProducts.objects.all()) == 0:
        for item in response.get('result').get('baseList'):
            fin_prdt_cd = item.get('fin_prdt_cd')
            # 이미 존재하는 상품인지 확인
            if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
                kor_co_nm = item.get('kor_co_nm')
                fin_prdt_nm = item.get('fin_prdt_nm')
                etc_note = item.get('etc_note')
                join_deny = item.get('join_deny')
                join_member = item.get('join_member')
                join_way = item.get('join_way')
                spcl_cnd = item.get('spcl_cnd')
                save_data = {
                    'fin_prdt_cd': fin_prdt_cd,
                    'kor_co_nm': kor_co_nm,
                    'etc_note': etc_note,
                    'fin_prdt_nm': fin_prdt_nm,
                    'join_deny': join_deny,
                    'join_member': join_member,
                    'join_way': join_way,
                    'spcl_cnd': spcl_cnd,
                }
                serializer_product = DepositSerializer(data=save_data)
                if serializer_product.is_valid(raise_exception=True):
                    serializer_product.save()

    # 옵션목록
    for item in response.get('result').get('optionList'):
        fin_prdt_cd = item.get('fin_prdt_cd')
        intr_rate_type_nm = item.get('intr_rate_type_nm')
        intr_rate = item.get('intr_rate')
        intr_rate2 = item.get('intr_rate2')
        save_trm = item.get('save_trm')
        # 이미 존재하는 상품에 대한 옵션인지 확인
        product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
        if product:
            if not DepositOptions.objects.filter(product=product, save_trm=save_trm).exists():
                save_data = {
                    'fin_prdt_cd': fin_prdt_cd,
                    'intr_rate_type_nm': intr_rate_type_nm,
                    'intr_rate': intr_rate,
                    'intr_rate2': intr_rate2,
                    'save_trm': save_trm,
                }
                serializer_option = DepositOptionSerializer(data=save_data)
                if serializer_option.is_valid():
                    serializer_option.save(product=product)

    return Response({'message': 'okay'})



# 받은 데이터 저장하기(예금, 예금에 대한 옵션)
@api_view(['GET'])
def export_data_to_json(request):
    # Query all DepositProducts and DepositOptions
    products = DepositProducts.objects.all()
    options = DepositOptions.objects.all()

    # Serialize the data
    products_json = serializers.serialize('json', products)
    options_json = serializers.serialize('json', options)

    # 경로 지정
    fixtures_dir = os.path.join(settings.BASE_DIR, 'financial', 'fixtures')

    # 만일 fixtures파일이 없다면 만들기
    if not os.path.exists(fixtures_dir):
        os.makedirs(fixtures_dir)

    # Write the serialized data to JSON files
    products_file_path = os.path.join(fixtures_dir, 'financial_depositproducts.json')
    options_file_path = os.path.join(fixtures_dir, 'financial_depositoptions.json')

    with open(products_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(products_json)

    with open(options_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(options_json)

    return Response({'message': 'Data exported to JSON files successfully'})


@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializers = DepositSerializer(products, many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = DepositSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"이미 있는 데이터이거나, 데이터가 잘못입력되었습니다."})



@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = product.depositoptions_set.all()
    serializers = DepositOptionSerializer(options,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def top_rate(request):
    option = DepositOptions.objects.order_by('-intr_rate2')[0]
    product = option.product
    serializer_option=DepositOptionSerializer(option)
    serializer_product=DepositSerializer(product)

    context = {
        'product':serializer_product.data,
        'option':serializer_option.data,
    }
    return Response(context)




@api_view(['GET'])
def combined_deposit_products(request):
    if request.method == "GET":
        products = DepositProducts.objects.all()
        serializer = CombinedDepositSerializer(products, many=True)
        return Response(serializer.data)




'''
여기부터는 적금
'''
url_saving = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
params_saving = {
    'auth':API_KEY,
    # 금융회사 코드
    'topFinGrpNo': '020000',
    'pageNo':1
}
def index(request):
    response = requests.get(url_saving,params=params_saving).json()
    return JsonResponse(response)




@api_view(['GET'])
def save_saving_products(request):
    response = requests.get(url_saving, params=params_saving).json()

    # 상품목록
    for item in response.get('result').get('baseList'):
        fin_prdt_cd = item.get('fin_prdt_cd')
        # 이미 존재하는 상품인지 확인
        if not SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            kor_co_nm = item.get('kor_co_nm')
            fin_prdt_nm = item.get('fin_prdt_nm')
            etc_note = item.get('etc_note')
            join_deny = item.get('join_deny')
            join_member = item.get('join_member')
            join_way = item.get('join_way')
            spcl_cnd = item.get('spcl_cnd')
            save_data = {
                'fin_prdt_cd': fin_prdt_cd,
                'kor_co_nm': kor_co_nm,
                'etc_note': etc_note,
                'fin_prdt_nm': fin_prdt_nm,
                'join_deny': join_deny,
                'join_member': join_member,
                'join_way': join_way,
                'spcl_cnd': spcl_cnd,
            }
            serializer_product = SavingSerializer(data=save_data)
            if serializer_product.is_valid(raise_exception=True):
                serializer_product.save()

    # 옵션목록
    for item in response.get('result').get('optionList'):
        fin_prdt_cd = item.get('fin_prdt_cd')
        intr_rate_type_nm = item.get('intr_rate_type_nm')
        intr_rate = item.get('intr_rate')
        intr_rate2 = item.get('intr_rate2')
        save_trm = item.get('save_trm')
        # 이미 존재하는 상품에 대한 옵션인지 확인
        product = SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
        if product:
            if not SavingOptions.objects.filter(product=product, save_trm=save_trm).exists():
                save_data = {
                    'fin_prdt_cd': fin_prdt_cd,
                    'intr_rate_type_nm': intr_rate_type_nm,
                    'intr_rate': intr_rate,
                    'intr_rate2': intr_rate2,
                    'save_trm': save_trm,
                }
                serializer_option = SavingOptionSerializer(data=save_data)
                if serializer_option.is_valid():
                    serializer_option.save(product=product)

    return Response({'message': 'okay'})




@api_view(['GET'])
def saving_products(request):
    if request.method == "GET":
        products = SavingProducts.objects.all()
        serializers = SavingSerializer(products, many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = SavingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message":"이미 있는 데이터이거나, 데이터가 잘못입력되었습니다."})


# 받은 데이터 저장하기(적금, 적금에 대한 옵션)
@api_view(['GET'])
def export_saving_data_to_json(request):
    products = SavingProducts.objects.all()
    options = SavingOptions.objects.all()

    # Serialize the data
    products_json = serializers.serialize('json', products)
    options_json = serializers.serialize('json', options)

    # 경로 지정
    fixtures_dir = os.path.join(settings.BASE_DIR, 'financial', 'fixtures')

    # 만일 fixtures파일이 없다면 만들기
    if not os.path.exists(fixtures_dir):
        os.makedirs(fixtures_dir)

    # Write the serialized data to JSON files
    products_file_path = os.path.join(fixtures_dir, 'financial_savingproducts.json')
    options_file_path = os.path.join(fixtures_dir, 'financial_savingoptions.json')

    with open(products_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(products_json)

    with open(options_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(options_json)

    return Response({'message': 'Data exported to JSON files successfully'})

@api_view(['GET'])
def saving_product_options(request,fin_prdt_cd):
    product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = product.savingoptions_set.all()
    serializers = SavingOptionSerializer(options,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def combined_saving_products(request):
    if request.method == "GET":
        products = SavingProducts.objects.all()
        serializer = CombinedSavingSerializer(products, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_financial_product(request,fin_prdt_cd):
    user = request.user

    if user.financial_products:
        financial_products = user.financial_products.split(',')
    else:
        financial_products = []

    # 상품 가입과 취소를 여기서 해결하자
    if fin_prdt_cd in financial_products:
        financial_products.remove(fin_prdt_cd)
        user.financial_products = ','.join(financial_products)
        user.save()
        return Response({"message": "가입 취소!"})
    
    financial_products.append(fin_prdt_cd)
    user.financial_products = ','.join(financial_products)
    user.save()

    return Response({"message": "가입 성공!"}, status=status.HTTP_200_OK)


################ 상품 추천 넣기#####################
import json
import numpy as np
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import joblib


# 모델과 라벨 인코더 로드
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'predict_model', 'random_forest_model.pkl')
encoder_path = os.path.join(BASE_DIR, 'predict_model', 'label_encoder.pkl')

loaded_model = joblib.load(model_path)
loaded_label_encoder = joblib.load(encoder_path)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # 입력 데이터를 데이터프레임으로 변환
        new_data = {
            'age': data['age'],
            'currentAsset': data['currentAsset'],
            'salary': data['salary'],
            'gender': data['gender']
        }
        new_df = pd.DataFrame([new_data])
        
        # 모델을 사용하여 예측 확률 얻기
        predicted_probabilities = loaded_model.predict_proba(new_df)
        
        # 예측된 확률과 레이블을 함께 저장할 리스트 생성
        predicted_results = []
        for label, prob in zip(loaded_model.classes_, predicted_probabilities[0]):
            predicted_results.append((label, prob))
        
        # 확률이 높은 순으로 정렬
        predicted_results.sort(key=lambda x: x[1], reverse=True)
        
        # 상위 5개 예측 결과 생성
        top_n_predictions = 5
        top_predictions = []
        for i in range(top_n_predictions):
            label, prob = predicted_results[i]
            predicted_product = loaded_label_encoder.inverse_transform([label])[0]
            top_predictions.append({'product': predicted_product, 'probability': prob})
        
        return JsonResponse({'predictions': top_predictions})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
