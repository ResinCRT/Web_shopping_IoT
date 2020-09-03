# 목록보기
from django.urls import path, re_path
# from order.views import CartLV, OrderLV
from shop.views import *
from . import views
app_name = 'cart'

urlpatterns = [
    # Example: /cart/
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    # Example: /order/
    path('', views.cart_detail, name='cart_detail'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
]
