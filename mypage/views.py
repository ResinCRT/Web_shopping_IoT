from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from shop.models import Order
from django.db.models import Q


# Create your views here.
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_order.html"


class ModifyUserView(LoginRequiredMixin, TemplateView):
    template_name = "mypage_modify_user.html"
    success_url = reverse_lazy('mypage:mypage_index')

class MyOrderView(LoginRequiredMixin, ListView):
    template_name = "mypage_order.html"
    model = Order
    paginate_by = 3
    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.pk)

class MyReviewView(LoginRequiredMixin, ListView):
    template_name = "mypage_review.html"
    success_url = reverse_lazy('mypage:mypage_index')

class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "mypage_wishlist.html"
    success_url = reverse_lazy('mypage:mypage_index')
