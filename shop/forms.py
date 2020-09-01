from django import forms
from .models import Qna
from .models import Product


class ProductSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')


class QnaForm(forms.Form):
    class Meta:
        model = Qna


class CartForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={'readonly':'readonly'}),
        error_messages={'required': "수량을 입력하세요."},
        label="수량"
    )
# class QnaForm(forms.ModelForm):
#     class Meta:
#         model = Qna
#         fields = ['qna_title','content']
#         widgets = {
#             'qna_title' : TextInput(attr={'class': 'input', 'placeholder': 'qna_title'}),
#             'content' : Textarea(attrs={'class': 'input', 'placeholder':'Your review'}),
#         }
