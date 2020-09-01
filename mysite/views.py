from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, TodayArchiveView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy




from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
import datetime

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        return context

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/ delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)