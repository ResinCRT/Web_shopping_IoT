from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_order.html"


class ModifyUserView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_modify_user.html"
    success_url = reverse_lazy('mypage:mypage_index')

class MyOrderView(LoginRequiredMixin, ListView):
    template_name = "mypage_order.html"
    success_url = reverse_lazy('mypage:mypage_index')

class MyReviewView(LoginRequiredMixin, ListView):
    template_name = "mypage_review.html"
    success_url = reverse_lazy('mypage:mypage_index')

class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "mypage_wishlist.html"
    success_url = reverse_lazy('mypage:mypage_index')
