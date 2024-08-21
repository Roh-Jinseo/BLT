from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('save-exchange-rates/', views.save_exchange_rates), #데이터 db저장용
    # path('exchange-rates/', views.exchange_rates), #데이터 db읽기
]
