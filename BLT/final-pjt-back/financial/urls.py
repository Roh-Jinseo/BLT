from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name = 'index'),
    path('save-deposit-products/',views.save_deposit_products),
    path('deposit-products/',views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/',views.deposit_product_options),
    path('deposit-products/top_rate/',views.top_rate),
    path('combined-deposit-products/', views.combined_deposit_products, name='combined_deposit_products'),
    # 파일 json으로 저장하기 위한 경로
    path('export_data_to_json/', views.export_data_to_json),
    # 여기부터 적금
    path('save-saving-products/',views.save_saving_products),
    path('saving-products/',views.saving_products),
    path('saving-product-options/<str:fin_prdt_cd>/',views.saving_product_options),
    path('combined-saving-products/', views.combined_saving_products, name='combined_saving_products'),
    # 파일 json으로 저장하기 위한 경로
    path('export_saving_data_to_json/', views.export_saving_data_to_json),
    path('join-product/<str:fin_prdt_cd>', views.join_financial_product, name='join-product'),
    path('predict/', views.predict, name='predict'),
]
