from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Qna, Review, ReviewAttachFile
from django.views.generic import CreateView, ListView, DetailView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q,Count
from shop.forms import ProductSearchForm, QnaForm
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from mysite.views import OwnerOnlyMixin
import os
from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect
# from .forms import QnaForm


# Create your views here.

# 상품 목록 출력
class ProductLV(ListView):
    model = Product
    template_name = 'shop/product_all.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_ordering(self):
        sortby = self.request.GET.get("sort", "-p_modify_dt")
        return sortby

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sortby = self.request.GET.get("sort", "-p_modify_dt")
        context["sortby"] = sortby
        return context


# 상품 상세 보기 출력
class ProductDV(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        product.read_cnt += 1
        product.save()
        return context

    # product_detail.html에서 접근할 때 product로 접근
    context_object_name = 'product'


# 검색창 통합검색 상품명, 브랜드명, 설명 다 포함해서 나오게
class SearchFormView(FormView):
    form_class = ProductSearchForm
    template_name = 'shop/product_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        product_list = Product.objects.filter(
            Q(p_name__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(brand__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = product_list
        return render(self.request, self.template_name, context)


# 질문 작성
class CreateQna(LoginRequiredMixin, CreateView):
    model = Qna
    fields = ['qna_title', 'content', 'author']
    # fields = ['qna_title', 'content', 'qna_create_date', 'qna_modify_date', 'author']

    # success_url = reverse_lazy('/shop/product/{product.id}')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs['product_id']
        # form.instance.qna_create_date = timezone.now()
        # form.instance.qna_modify_date = timezone.now()
        response = super().form_valid(form)

        return response

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})


# 질문 수정
class UpdateQnaView(OwnerOnlyMixin, UpdateView):
    model = Qna
    fields = ['qna_title', 'content']
    # success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        form.instance.modify_dt = timezone.now()
        delete_files = self.request.POST.getlist("delete_files")
        for file in delete_files:
            file = QnaAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)
            file.delete()

        response = super().form_valid(form)

        return response

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})


# 질문 삭제
class DeleteQnaView(OwnerOnlyMixin, DeleteView):
    model = Qna

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})


# 질문 삭제(팝업창으로)
def remove_qna(request, qna_id):
    qna = Qna.objects.get(id=qna_id, author_id=request.user.id)
    qna.delete()
    return HttpResponseRedirect(reverse('shop:detail', kwargs={'pk': qna.product_id}))






# 질문 덧글
class QnaComment(LoginRequiredMixin, CreateView):
    model = Qna
    fields = ['qna_title', 'content', 'author']

    # success_url = reverse_lazy('/shop/product/{product.id}')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs['product_id']
        form.instance.parent_id = self.kwargs['qna_id']
        # form.instance.qna_create_date = timezone.now()
        # form.instance.qna_modify_date = timezone.now()
        response = super().form_valid(form)

        return response

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})



# 해당 상품 리뷰 목록
class ReviewLV(ListView):
    model = Review


# 리뷰 작성
class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['review_title','rating', 'content']

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs['pk']
        form.instance.r_created_dt = timezone.now()
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = ReviewAttachFile(review=self.object, filename=file.name,
                                            size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()

        return response





# 리뷰 수정
class UpdateReviewView(OwnerOnlyMixin, UpdateView):
    model = Review
    fields = ['review_title','rating', 'content']

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})

    def form_valid(self, form):
        form.instance.r_modify_dt = timezone.now()
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:
            file = ReviewAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)
            file.delete()

        response = super().form_valid(form)
        files = self.request.FILES.getlist("files")

        for file in files:
            attach_file = ReviewAttachFile(review=self.object, filename=file.name,
                                            size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()

        return response


# 리뷰 삭제
class DeleteReviewView(OwnerOnlyMixin, DeleteView):
    model = Review

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk': self.object.product_id})


# 리뷰 삭제(팝업창으로)
def remove_review(request, review_id):
    review = Review.objects.get(id=review_id, author_id=request.user.id)
    review.delete()
    return HttpResponseRedirect(reverse('shop:detail', kwargs={'pk': review.product_id}))
