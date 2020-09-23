from django import forms
from .models import CartItem
from django.db import models

# class AddToCartForm(forms.Form):
#     # 상품 수량 설정 field
#     quantity = forms.IntegerField(initial=1)


class AddToCartForm(forms.ModelForm):
    # 상품 수량 설정 field
    class Meta:
        model = CartItem
        fields = ['quantity']
