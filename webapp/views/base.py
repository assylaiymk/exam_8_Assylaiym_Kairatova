from django.views.generic import ListView
from urllib.parse import urlencode
from django.db.models import Q
from webapp.forms import SearchForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)
    # allow_empty = False
    # queryset = Article.objects.exclude(status=StatusChoices.NOT_ACTIVE)
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_from()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_from(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context