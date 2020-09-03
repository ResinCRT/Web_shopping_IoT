# 목록보기
from django.urls import path, re_path
# from order.views import CartLV, OrderLV
from shop.views import *
from . import views
app_name = 'cart'

urlpatterns = [
    # Example: /order/
    path('', views.cart_detail, name='cart_detail'),
    # Example: /cart/add/<int:product_id>
    path('addtocart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Example: /cart/minus/<int:product_id>
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    # Example: /cart/minus/<int:product_id>
    path('minus/<int:product_id>/', views.minus_cart, name='minus_cart'),
    # Example: /cart/remove_cart/<int:product_id>
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
]
