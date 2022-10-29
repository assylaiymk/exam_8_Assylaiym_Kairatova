from django.views.generic import ListView

from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)
    allow_empty = True
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_deleted=False)
        return context
