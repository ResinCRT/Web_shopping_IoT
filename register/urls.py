from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from register.views import UserCreateView, UserCreateDoneTV

app_name = 'register'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserCreateView.as_view(), name='sign_up'),
    path('register/done/', UserCreateDoneTV.as_view(), name='sign_up_done'),
]