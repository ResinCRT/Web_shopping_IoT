"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
from mysite.views import HomeView
import datetime
from shop.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('mypage/', include('mypage.urls')),
    path('accounts/', include('register.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('shop/', include('shop.urls')),

    path('shop/', ProductLV.as_view(),name='index'),
    path('shop/product/', ProductLV.as_view(), name='index'),
    path('shop/product/<int:pk>/add_qna', CreateQna.as_view(), name='qna'),

    path('cart/', include('cart.urls', 'cart')),
    path('order/', include('order.urls', 'order')),

    ]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
