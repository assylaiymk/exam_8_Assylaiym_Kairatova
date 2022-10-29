from django.contrib.auth.models import User
from django.db import models

from webapp.models.products import Product


class Review(models.Model):
    author = models.ForeignKey(to=User, verbose_name='Author', null=False, related_name='author', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', blank=True, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text', max_length=3000, null=False, blank=False)
    rating = models.FloatField(verbose_name='Rating', blank=False)

    def __str__(self):
        return f'{self.author} - {self.product}, {self.text}, {self.rating}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
