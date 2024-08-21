import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ExchangeRates
from .serializers import ExchangeRatesSerializer

# Create your views here.
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
BASE_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

def save_exchange_rates(request):
    # requests 모듈을 활용하여 환율 정보 받아오기
    # URL = BASE_URL 
    params = {
       'authkey' : EXCHANGE_API_KEY,
       'searchdate' : '20240514',
       'data' : 'AP01'
    }
    response = requests.get(BASE_URL, params=params).json()
    # print(response)

    for rate in response:
        exchange_rate_data = {
            'result' : rate.get('result'),
            'cur_unit' : rate.get('cur_unit'),
            'ttb' : rate.get('ttb'),
            'tts' : rate.get('tts'),
            'deal_bas_r' : rate.get('deal_bas_r'),
            'bkpr' : rate.get('bkpr'),
            'yy_efee_r' : rate.get('yy_efee_r'),
            'ten_dd_efee_r' : rate.get('ten_dd_efee_r'),
            'kftc_deal_bas_r' : rate.get('kftc_deal_bas_r'),
            'kftc_bkpr' : rate.get('kftc_bkpr'),    
            'cur_nm' : rate.get('cur_nm'),
        }
        serializer = ExchangeRatesSerializer(data=exchange_rate_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        
    return JsonResponse({'response':response})


# # db데이터 불러오기
# @api_view(['GET'])
# def exchange_rates(request):
#     if request.method == 'GET':
#         exchange_rates = ExchangeRates.objects.all()
#         serializer = ExchangeRatesSerializer(exchange_rates, many=True)
#         return Response(serializer.data)
    