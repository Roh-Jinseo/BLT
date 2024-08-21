from django.db import models

# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True, default = '없음') # 금융상품코드
    kor_co_nm = models.TextField(default = '없음') # 금융회사명
    fin_prdt_nm = models.TextField(default = '없음') # 금융상품명
    etc_note = models.TextField(default = '없음') # 금융 상품설명
    join_deny = models.IntegerField(default = -1) # 가입제한
    join_member = models.TextField(default = '없음') # 가입데상
    join_way = models.TextField(default = '없음') # 가입방법
    spcl_cnd = models.TextField(default = '없음') # 우대조건
    def __str__(self):
        return self.fin_prdt_nm

    

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete = models.CASCADE) # 외래키 위에서 가져오기 
    fin_prdt_cd = models.TextField(default = '없음') # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length = 100,default = '없음') # 저축금리 유형명
    intr_rate = models.FloatField(default = -1)  # 저축금리
    intr_rate2 = models.FloatField(default = -1)  # 최고우대금리
    save_trm = models.IntegerField(default = -1)  # 저축기간(월단위)

    def __str__(self):
        return f"{self.product.fin_prdt_nm} - {self.intr_rate_type_nm}"

from django.db import models

# Create your models here.

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True, default = '없음') # 금융상품코드
    kor_co_nm = models.TextField(default = '없음') # 금융회사명
    fin_prdt_nm = models.TextField(default = '없음') # 금융상품명
    etc_note = models.TextField(default = '없음') # 금융 상품설명
    join_deny = models.IntegerField(default = -1) # 가입제한
    join_member = models.TextField(default = '없음') # 가입데상
    join_way = models.TextField(default = '없음') # 가입방법
    spcl_cnd = models.TextField(default = '없음') # 우대조건
    def __str__(self):
        return self.fin_prdt_nm

    

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete = models.CASCADE) # 외래키 위에서 가져오기 
    fin_prdt_cd = models.TextField(default = '없음') # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length = 100,default = '없음') # 저축금리 유형명
    intr_rate = models.FloatField(default = -1)  # 저축금리
    intr_rate2 = models.FloatField(default = -1)  # 최고우대금리
    save_trm = models.IntegerField(default = -1)  # 저축기간(월단위)
    

    def __str__(self):
        return f"{self.product.fin_prdt_nm} - {self.intr_rate_type_nm}"
