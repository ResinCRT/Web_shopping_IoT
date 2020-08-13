from django.shortcuts import render

# Create your views here.

# 상품 목록 출력
class ProductLV(ListView):
    model = Product
    template_name = 'shop/procduct_all.html'
    context_object_name = 'products'
    # 한페이지에 보여줄 문서 건수는 상의하기

# 상품 상세 보기 출력
class ProductDV(DetailView):
    model = Product

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object