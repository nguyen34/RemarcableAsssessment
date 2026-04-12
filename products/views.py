from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.
class ProductListView(ListView):
    """Renders the product page, with a list of products."""

    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context

    
