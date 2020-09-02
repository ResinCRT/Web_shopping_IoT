from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, TodayArchiveView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from shop.models import *



from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
import datetime

class HomeView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = "products"
    paginate_by = 8

    def get_ordering(self):
        sortby = "-read_cnt"
        return sortby

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sortby = "-read_cnt"
        context["sortby"] = sortby
        return context

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/ delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)