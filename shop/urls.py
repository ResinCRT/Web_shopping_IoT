# 목록보기
from django.urls import path, re_path
from django.conf.urls import url

from shop.views import *
# from .views import *
app_name = 'shop'

urlpatterns = [
    # Example: /shop/
    path('', ProductLV.as_view(), name='index'),
    # Example: /shop/product/product_id
    path('product/<int:pk>/', ProductDV.as_view(), name='detail'),
    # Example: /shop/search/
    path('search/', SearchFormView.as_view(), name='search'),

    # Example: /shop/product/product_id/qna/add/
    path('product/<int:product_id>/qna/add/', CreateQna.as_view(), name='add_qna'),
    # Example: /shop/qna/<id>/update/
    path('qna/<int:pk>/update/', UpdateQnaView.as_view(), name='update_qna'),
    # Example: /shop/qna/<id>/delete/
    path('qna/<int:pk>/delete/', DeleteQnaView.as_view(), name='delete_qna'),
    # Example: /shop/qna/<id>/delete/
    path('qna/<int:qna_id>/remove/', remove_qna, name='remove_qna'),

    # Example: /shop/product/product_id/qna/add/comment/<qna_id>
    path('product/<int:product_id>/qna/add/comment/<int:qna_id>/', QnaComment.as_view(), name='add_comment'),

    # Example: /shop/product/id/review/add/
    path('product/<int:pk>/review/add/', CreateReviewView.as_view(), name='add_review'),
    # Example: /shop/review/id/update/
    path('review/<int:pk>/update/', UpdateReviewView.as_view(), name='update_review'),
    # Example: /shop/review/id/delete/
    path('review/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),
    # Example: /shop/review/<id>/remove/
    path('review/<int:review_id>/remove/', remove_review, name='remove_review'),
]