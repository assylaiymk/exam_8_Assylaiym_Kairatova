from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
from webapp.models import Product, Review


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError('Maximum length of string is 20 symbols')
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20, message=''):
        message = 'Maximum value %(limit_value)s you entered %(show_value)s values'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=123,
                            label='Title',
                            validators=(
                                MinLengthValidator(limit_value=2, message='aaaa'),
                                CustomLengthValidator(limit_value=10),
                                )
                            )

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

