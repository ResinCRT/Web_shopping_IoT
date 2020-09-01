from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from register.forms import UserChangeForm
from django.urls import reverse_lazy
from shop.models import *
from order.models import *
from django.db.models import Q


# Create your views here.
class ModifyUserView(LoginRequiredMixin, FormView):
    template_name = "mypage/mypage_modify_user.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('mypage:mypage_index')

    def get_form(self):
        form = super(ModifyUserView, self).get_form()
        form.fields['addr'].widget.attrs.update({'value': self.request.user.addr})
        form.fields['phone'].widget.attrs.update({'value': self.request.user.phone})
        form.fields['birthdate'].widget.attrs.update({'value': self.request.user.birthdate})
        return form

    def form_valid(self, form):
        response = super().form_valid(form)
        Users = self.request.user
        Users.addr = form.instance.addr
        Users.birthdate = form.instance.birthdate
        Users.phone = form.instance.phone
        Users.save()
        return response

class PwChangeView(auth_views.PasswordChangeView):
    template_name = "mypage/mypage_password_change.html"
    success_url = reverse_lazy('register:password_change_done')

class MyOrderView(LoginRequiredMixin,ListView):
    template_name = "mypage/mypage_order.html"
    model = Order
    context_object_name = "order"
    paginate_by = 3
    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.pk).select_related("product_id")

class MyReviewView(LoginRequiredMixin, ListView):
    template_name = "mypage/mypage_review.html"
    model = Review
    context_object_name = "review"
    paginate_by = 3
    def get_queryset(self):
        return Review.objects.filter(user_id=self.request.user.pk).select_related("product_id")

class MyWishlistView(LoginRequiredMixin, ListView):
    template_name = "myapge/mypage_wishlist.html"

