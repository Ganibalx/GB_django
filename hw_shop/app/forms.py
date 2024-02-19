from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['data_add']
        labels = {'name': 'Название',
                  'description': 'Описание',
                  'price': 'Цена',
                  'count': 'кол-во',
                  'img': 'Изображение'}

