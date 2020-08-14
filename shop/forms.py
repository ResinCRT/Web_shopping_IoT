from django import forms

class ProductSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
