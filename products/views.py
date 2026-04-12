from django.shortcuts import render
from products.models import Product
from products.forms import ProductFilterForm
from django.views.generic import ListView

# Create your views here.
class ProductListView(ListView):
    """Renders the product page, with a list of products."""

    model = Product

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get('query')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        if query:
            qs = qs.filter(description__icontains=query)
        if category:
            qs = qs.filter(category=category)
        if tag:
            qs = qs.filter(tags=tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        initial_data = {
            'query': query,
            'tag': tag,
            'category': category
        }
        context['form'] = ProductFilterForm(initial=initial_data)
        return context

    
