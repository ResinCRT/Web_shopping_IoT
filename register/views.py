from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, TodayArchiveView
from register.forms import *
from django.urls import reverse_lazy,path
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views
# Create your views here.
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register:sign_up_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class PwChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('register:password_change_done')

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/ delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)


