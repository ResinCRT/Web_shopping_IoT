from django.shortcuts import render
from shop.models import Product,Brand
from django.views.generic import ListView,DetailView,FormView
from django.db.models import Q
from shop.forms import ProductSearchForm
# Create your views here.

# 상품 목록 출력
class ProductLV(ListView):
    model = Product
    template_name = 'shop/procduct_all.html'
    context_object_name = 'products'
    paginate_by = 3
    
    # 한페이지에 보여줄 문서 건수는 상의하기
    
    #so는 그냥 임시 파라미터 이름
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

