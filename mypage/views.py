from django.shortcuts import render
from django.views.generic import ListView,TemplateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from register.forms import UserChangeForm
from django.urls import reverse_lazy
from shop.models import *
from order.models import *
from mysite.views import OwnerOnlyMixin
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

class MyOrderDV(OwnerOnlyMixin,DetailView):
    template_name = "mypage/mypage_order_detail.html"
    context_object_name = "order"
    model = Order
    def get_context_data(self, **kwargs):
        detail = OrderDetail.objects.select_related("order").filter(order__id=self.object.pk)
        context = super().get_context_data(**kwargs)
        context['details'] = detail
        return context


class MyOrderView(LoginRequiredMixin,ListView):
    template_name = "mypage/mypage_order_2.html"
    context_object_name = "order"
    paginate_by = 3

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.pk).order_by('-order_dt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_sum = Q()
        for ord in context['order']:
            query_sum = query_sum | Q(order__id=ord.id)
        if query_sum:
            context['order_detail'] = OrderDetail.objects.select_related("order").filter(query_sum)
        return context


class MyReviewView(LoginRequiredMixin, ListView):
    template_name = "mypage/mypage_review.html"
    model = Review
    context_object_name = "reviews"
    paginate_by = 3
    def get_queryset(self):
        return Review.objects.filter(author=self.request.user.pk)

class MyQnaView(LoginRequiredMixin, ListView):
    template_name = "mypage/mypage_qna.html"
    model = Review
    paginate_by = 3
    context_object_name = "qnas"
    def get_queryset(self):
        return Qna.objects.filter(Q(author=self.request.user.pk) & Q(parent__isnull=True)).select_related("product")

