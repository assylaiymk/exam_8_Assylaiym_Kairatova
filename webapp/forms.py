from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'image')

    def clean_tite(self):
        title = self.cleaned_data('title')
        if Product.objects.filter(title=title).exists():
            raise ValidationError('Product with this title already exists')

        return title


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('author', 'product', 'text', 'rating')
