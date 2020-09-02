from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, TodayArchiveView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from shop.models import *
from order.models import *
from django.http import Http404
from django.utils.translation import gettext as _

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

class CategoryView(DetailView):
    model = Category
    template_name = "shop/product_all.html"

    def get_object(self, queryset=None):

        # override get_object in SingleObjectMixin
        # URL pattern : .../category/<parent>+<pk>
        # if you clicked parent, search all products whose parent category is <parent>
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        parent = self.kwargs.get('parent')

        # check pk
        if pk is not '0':
            print("pk is not 0")
            queryset = queryset.filter(pk=pk)
        else:
            print("pk is 0")
            queryset = queryset.filter(pk=int(parent))

        # If none of those are defined, it's an error.
        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = {}
        if self.kwargs['pk'] == '0':
            context['products'] = Product.objects.select_related('category').filter(category__parent_id=self.kwargs['parent'])
        else:
            context['products'] = Product.objects.select_related('category').filter(category=self.object.pk)

        return context

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/ delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if type(self.object) == type(Product.objects.first()):
            owner = self.object.author
        elif type(self.object) == type(OrderDetail.objects.first()):
            owner = self.object.order.user
        elif type(self.object) == type(Order.objects.first()):
            owner = self.object.user

        if self.request.user != owner:
            self.handle_no_permission()

        return super().get(request, *args, **kwargs)

def category_context_processor(request):
    context = {
        'categories': Category.objects.all()
    }
    return context
