from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from register.views import *

app_name = 'register'

urlpatterns = [
    path('password_change/',PwChangeView.as_view(), name='password_change'),
    path('', include('django.contrib.auth.urls')),
    path('register/', UserCreateView.as_view(), name='sign_up'),
    path('register/done/', UserCreateDoneTV.as_view(), name='sign_up_done'),
]
