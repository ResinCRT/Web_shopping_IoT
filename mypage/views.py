from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from register.forms import UserChangeForm
from django.urls import reverse_lazy
from shop.models import *
from django.db.models import Q


# Create your views here.


class ModifyUserView(LoginRequiredMixin, FormView):
    template_name = "mypage_modify_user.html"
    form_class = UserChangeForm
    model = User
    context_object_name = "users"
    success_url = reverse_lazy('mypage:mypage_index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(self,**kwargs)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return response



class MyOrderView(LoginRequiredMixin,ListView):
    template_name = "mypage_order.html"
    model = Order
    context_object_name = "order"
    paginate_by = 3
    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.pk).select_related("product_id")

class MyReviewView(LoginRequiredMixin, ListView):
    template_name = "mypage_review.html"
    model = Review
    context_object_name = "review"
    paginate_by = 3
    def get_queryset(self):
        return Review.objects.filter(user_id=self.request.user.pk).select_related("product_id")

class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "mypage_wishlist.html"

