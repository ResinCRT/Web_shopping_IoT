# 목록보기
from django.urls import path, re_path
from order.views import *
from shop.views import *
from . import views


app_name = 'order'

urlpatterns = [
    # Example: /order/<int:pk>
    path('add/<int:cart_id>', views.cart_to_order, name='cart_to_order'),
    path('', views.order_detail, name='detail_order'),
    path('order_list/', views.order_view, name='order_view'),
]

