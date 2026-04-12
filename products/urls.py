from django.urls import path
from products import views
from products.models import Product

product_list_view = views.ProductListView.as_view(
    queryset=Product.objects.order_by("name"),  # :5 limits the results to the five most recent
    context_object_name="product_list",
    template_name="products/product.html",
)

urlpatterns = [
    path("", product_list_view, name="product"),
]