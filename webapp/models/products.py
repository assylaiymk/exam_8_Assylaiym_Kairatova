from django.db import models
from django.db.models import TextChoices
from django.utils import timezone

from webapp.managers import ProductManager


class StatusChoices(TextChoices):
    MEAT = 'MEAT', 'Meat'
    VEGAN = 'VEGAN', 'Vegan'


class Product(models.Model):
    title = models.TextField(verbose_name='Title', max_length=100, null=False, blank=False)
    category = models.CharField(verbose_name='Category', choices=StatusChoices.choices, max_length=200,
                                default=StatusChoices.MEAT)
    description = models.TextField(verbose_name='Description', max_length=2000, blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='products',
        verbose_name='Image'
    )
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)

    objects = ProductManager()

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
