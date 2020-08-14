from django.shortcuts import render
from shop.models import Product,Brand,Qna,Review,ProductAttachFile
from django.views.generic import CreateView,ListView,DetailView,FormView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from shop.forms import ProductSearchForm
from django.urls import reverse_lazy
from django.utils import timezone
from mysite.views import OwnerOnlyMixin
import os
from django.conf import settings


# Create your views here.

# 상품 목록 출력
class ProductLV(ListView):
    model = Product
    template_name = 'shop/procduct_all.html'
    context_object_name = 'products'
    paginate_by = 3
    
    # 한페이지에 보여줄 문서 건수는 상의하기
    # so는 그냥 임시 파라미터 이름
    # if so == 'recommend':
    #     product_list = Product.objects.order_by('-read_cnt','-create_dt') #조회수순
    # elif so == 'price':
    #     product_list = Product.objects.order_by('-price','-create_dt') #가격순
    # else:
    #     product_list = Product.objects.order_by('-create_dt')  #최신순

    context = {}

# 상품 상세 보기 출력


class ProductDV(DetailView):
    model = Product

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        product.read_cnt += 1
        product.save()
        return context

    #product_detail.html에서 접근할 때 product로 접근
    context_object_name = 'product'


# 검색창 통합검색 상품명, 브랜드명, 설명 다 포함해서 나오게
class SearchFormView(FormView):
    form_class = ProductSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        product_list = Product.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)|
            Q(brand__icontains=searchWord)
            ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = product_list
        return render(self.request, self.template_name, context)


class CreateQna(LoginRequiredMixin, CreateView):
    model = Qna
    fields = ['Qna_title', 'content', 'content', 'tags']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now()
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = ProductAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class QnaUpdateView(OwnerOnlyMixin, UpdateView):
    model = Product
    fields = ['Qna_title', 'content', 'content', 'tags']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.modify_dt = timezone.now()

        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:
            file = ProductAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)
            file.delete()

        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = ProductAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class QnaDeleteView(OwnerOnlyMixin, DeleteView):
    model = Qna
    success_url = reverse_lazy('shop:index')


class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['Review_title', 'content', 'content', 'tags']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now()
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = ProductAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class ReviewUpdateView(OwnerOnlyMixin, UpdateView):
    model = Product
    fields = ['Qna_title', 'content', 'content']
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.modify_dt = timezone.now()

        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:
            file = ProductAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)
            file.delete()

        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = ProductAttachFile(post=self.object, filename=file.name,
                                         size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response


class ReviewDeleteView(OwnerOnlyMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('shop:index')