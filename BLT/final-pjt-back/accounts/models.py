from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
	

class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    age = models.IntegerField()
    currentAsset = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    gender = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])  # 0: Female, 1: Male
    img = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    financial_products = models.TextField() #사용자가 가입한 상품목록 저장할 필드 

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data.get("email")
        user.username = data.get("username")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.nickname = data.get("nickname")
        user.age = data.get("age")
        user.currentAsset = data.get("currentAsset")
        user.salary = data.get("salary")
        user.gender = data.get("gender")
        # 추가부분###################
        user.img = data.get("img")
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user
