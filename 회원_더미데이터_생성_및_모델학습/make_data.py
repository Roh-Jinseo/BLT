# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
"""


import random
import requests

first_name_samples = '김이박최정강조윤장임한오서신권황안송전홍노'
middle_name_samples = '민서예지도하주윤채현지유수인장가한'
last_name_samples = '준윤우원호후서연아은진영나람'

username_samples1 = ['Bii', 'Aix', 'Bov', 'Cez', 'Dix', 'Eum', 'Fow', 'Gak', 'Huv', 'Iqe', 'Jux', 'Koz', 'Lyp', 'Mib', 'Nod', 'Opk', 'Pug', 'Qaz', 'Rim', 'Sop', 'Tuv', 'Ujx', 'Vex', 'Wip', 'Xob', 'Yud', 'Zig', 'Aov', 'Bex', 'Cim', 'Duk', 'Efx', 'Fuq', 'Gob', 'Hax', 'Ize', 'Joc', 'Kep', 'Lut', 'Maw', 'Nir', 'Obx', 'Pij', 'Qop', 'Rax', 'Siv', 'Tez', 'Uvo', 'Vix', 'Wuq', 'Xil', 'Yob', 'Zep', 'Auz', 'Bik', 'Cov', 'Diz', 'Eak', 'Fum', 'Giz', 'Hoq', 'Ivx', 'Jub', 'Kif', 'Lom', 'Mep', 'Nux', 'Ove', 'Pij', 'Qex', 'Rop', 'Suz', 'Tib', 'Ulk', 'Vot', 'Weg', 'Xut', 'Yix', 'Zod', 'Aex', 'Biq', 'Cuf', 'Dir', 'Eix', 'Fuz', 'Gax', 'Hep', 'Iok', 'Juz', 'Kob', 'Lip', 'Mik', 'Nuz', 'Ozv', 'Oxy', 'Cal', 'Cor', 'Zoo', 'kee', 'Bey']
username_samples2 = ['Ab', 'Cd', 'Ef', 'Gh', 'Ij', 'Kl', 'Wx', 'Yz', 'Ba', 'Ce', 'Dh', 'Fi', 'Gk', 'Ln', 'Mo', 'Pr', 'Qs', 'Tu', 'Vw', 'Xy', 'Za', 'Bd', 'Cf', 'Eh', 'Gi', 'Jk', 'Lm', 'No', 'Pq', 'Rs', 'Tv', 'Uw', 'Xz', 'Yb', 'Ac', 'De', 'Fg', 'Hi', 'Jm', 'Kn', 'Lo', 'Mp', 'Qr', 'St', 'Uw', 'Xv', 'Ya', 'Bc', 'Ed', 'Fg', 'Ha', 'Ji', 'Lk', 'Mn', 'Op', 'Qe', 'Rs', 'Tu', 'Vx', 'Wy', 'Za', 'Db', 'Ce', 'Hg', 'Fi', 'Jk', 'Lm', 'Np', 'Oq', 'Sr', 'Ut', 'Vw', 'Xy', 'Zz', 'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy','Zz']

nickname_sample = ['가람', '가온', '강이', '건이', '겨울', '고운', '구름', '기쁨', '나래', '나무', '나은', '달빛', '달이', '단비', '다온', '다정', '도도', '도란', '두리', '라온', '루다', '루리', '마루', '망고', '모모', '미소', '바다', '바름', '바오', '반디', '별이', '봄이', '부엉', '비비', '빵이', '사랑', '새봄', '새벽', '소리', '솔이', '수리', '마일', '시우', '아라', '아미', '아토', '아하', '알콩', '애리', '에코', '연이', '열매', '온유', '온이', '와니', '우주', '율리', '은이', '이안', '이루', '이삭', '이솔', '인디', '자두', '자몽', '장미', '재롱', '조이', '주니', '쭈니', '초롱', '초코', '치즈', '코코', '키위', '태양', '토리', '토토', '티나', '파랑', '파티', '펄이', '포도', '푸름', '하람', '하리', '하민', '하빈', '하랑', '하율', '하임', '하준', '한별', '한솔', '햇살', '호두', '희망']


def random_name(): #random username
    result = ''
    result += random.choice(username_samples1)
    result += random.choice(username_samples2)
    # result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

def random_last():
    result = random.choice(last_name_samples)
    return result 

def random_first():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    return result

def random_nickname():
    result = ''
    result += random.choice(nickname_sample)
    result += random.choice(nickname_sample)
    return result


# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = 'b3aeed93b99caeb861d7349f1e14dadd'

financial_products = []

params = {
    'auth': API_KEY,
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
    'topFinGrpNo': '020000',
    'pageNo': 1,
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# print(baseList)
print(financial_products)
dict_keys = [
    'username',
    'last_name',
    'first_name',
    'gender',
    'financial_products',
    'age',
    'money',
    'salary',
]

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
last_name_list = []
first_name_list = []
nickname_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1
    
    #randomly generate last name 
    rl = random_last()
    last_name_list.append(rl)

    #randomly generate first name 
    rf = random_first()
    first_name_list.append(rf)

    #randomly generate nickname 
    rnn = random_nickname()
    nickname_list.append(rnn)



# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
# save_dir = '../backend/accounts/fixtures/accounts/user_data.json'
save_dir = 'users_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    for i in range(N):
        # 랜덤한 데이터를 삽입
        # file['model'] = 'accounts.User'
        # file['pk'] = i + 1
        file['fields'] = {
            'username': username_list[i],  # username 랜덤 생성
            'last_name' : last_name_list[i], # 유저 성 랜덤생성
            'first_name' : first_name_list[i], # 유저 이름 랜덤생성
            'nickname':  nickname_list[i], #nickname 랜덤생성

            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            'financial_products': ','.join(
                [
                    random.choice(financial_products)
                    for _ in range(random.randint(0, 5))
                ]
            ),  # 금융 상품 리스트
            'age': random.randint(1, 100),  # 나이
            'currentAsset': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000),  # 연봉
            'password': '1234',
            'gender':random.randint(0,1), #성별
            # 'is_active': True,
            # 'is_staff': False,
            # 'is_superuser': False,
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
