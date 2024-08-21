from django.db import models

# Create your models here.
# RESULT	Integer	조회 결과	1 : 성공, 2 : DATA코드 오류, 3 : 인증코드 오류, 4 : 일일제한횟수 마감
# CUR_UNIT	String	통화코드	
# CUR_NM	String	국가/통화명	
# TTB	String	전신환(송금) 받으실때	
# TTS	String	전신환(송금) 보내실때	
# DEAL_BAS_R	String	매매 기준율	
# BKPR	String	장부가격	
# YY_EFEE_R	String	년환가료율	
# TEN_DD_EFEE_R	String	10일환가료율	
# KFTC_DEAL_BAS_R	String	서울외국환중개  매매기준율	
# KFTC_BKPR	String	서울외국환중개 장부가격

# from django.db import models

class ExchangeRates(models.Model):
    result = models.IntegerField()
    cur_unit = models.CharField(max_length=10)  # Assuming currency unit codes are not longer than 10 characters
    cur_nm = models.CharField(max_length=100)  # Assuming currency names are not longer than 100 characters
    ttb = models.CharField(max_length=20)  # Assuming the buy rate is stored as a string (to preserve formatting)
    tts = models.CharField(max_length=20)  # Assuming the sell rate is stored as a string (to preserve formatting)
    deal_bas_r = models.CharField(max_length=20)  # Assuming the base rate is stored as a string (to preserve formatting)
    bkpr = models.CharField(max_length=20)  # Assuming the bank buying rate is stored as a string (to preserve formatting)
    yy_efee_r = models.CharField(max_length=20, null=True, blank=True)  # Assuming the yearly fee rate is optional
    ten_dd_efee_r = models.CharField(max_length=20, null=True, blank=True)  # Assuming the 10-day fee rate is optional
    kftc_deal_bas_r = models.CharField(max_length=20, null=True, blank=True)  # Assuming the KFTC base rate is optional
    kftc_bkpr = models.CharField(max_length=20, null=True, blank=True)  # Assuming the KFTC bank buying rate is optional

    def __str__(self):
        return f"{self.cur_nm} ({self.cur_unit}): {self.deal_bas_r}"
