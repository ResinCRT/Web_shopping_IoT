from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic import CreateView, TodayArchiveView
from register.forms import *
from django.urls import reverse_lazy, path, reverse
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import get_messages
# Create your views here.
class UserCreateView(SuccessMessageMixin,CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register:sign_up_done')
    def form_valid(self, form):
        response = super(UserCreateView, self).form_valid(form)
        self.request.session['success_id'] = self.request.POST.get('username')
        self.request.session['success_name'] = self.request.POST.get('real_name')
        self.request.session['success_email'] = self.request.POST.get('email')
        return response


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['username'] = self.request.session.get('success_id')
        context['real_name'] = self.request.session.get('success_name')
        context['email'] = self.request.session.get('success_email')
        return context


class PwChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('register:password_change_done')
    def form_valid(self,form):
        response = super().form_valid(form)
        return response

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/ delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)


