from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_main.html"


class ModifyUserView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_modify_user.html"
    success_url = reverse_lazy('mypage:mypage_index')

