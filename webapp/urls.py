from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductCreate, ProductUpdateView, ProductDeleteView, ProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/add/', ProductCreate.as_view(), name='product_add'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/', IndexView.as_view()),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail')
]