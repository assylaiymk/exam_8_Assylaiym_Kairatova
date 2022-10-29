from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class ProductCreate(LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['user', 'admin']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = 'review_create.html'
    form_class = ReviewForm
    model = Review

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})


class ReviewView(DetailView):
    template_name = 'review.html'
    model = Review


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'review_update.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    groups = ['user', 'admin']

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')


