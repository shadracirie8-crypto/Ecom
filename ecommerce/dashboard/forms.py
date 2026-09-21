from django import forms

from shop.models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [

            'title',
            'price',
            'description',
            'Category',
            'image',
            'stock'

        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500 h-40 resize-none'
            }),

            'Category': forms.Select(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500'
            }),

            'image': forms.FileInput(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500 bg-white'
            }),

            'stock': forms.NumberInput(attrs={
                'class': 'w-full rounded-2xl border border-gray-200 px-5 py-4 outline-none focus:border-indigo-500'
            }),

        }