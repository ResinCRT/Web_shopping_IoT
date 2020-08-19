from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
from mypage.views import *

app_name = "mypage"

urlpatterns = [
    path('', MypageView.as_view(), name="mypage_index"),
    path('modify/', ModifyUserView.as_view(), name="modify_user"),

]