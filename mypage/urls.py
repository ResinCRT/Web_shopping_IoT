from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
from mypage.views import *
from order.views import *

app_name = "mypage"

urlpatterns = [
    path('', MyOrderView.as_view(), name="mypage_index"),
    path('order/', MyOrderView.as_view(), name="order"),
    path('order_list/', order_view, name='order2'),
    path('order/<int:pk>/', MyOrderDV.as_view(), name='order_detail'),
    path('reviews/', MyReviewView.as_view(), name="review"),
    path('qna/', MyQnaView.as_view(), name="qna"),
    path('modify/', ModifyUserView.as_view(), name="modify_user"),
    path('modify/change_password',PwChangeView.as_view(),name="pw_change")

]