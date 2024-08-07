from django.shortcuts import render
from django.views.generic import TemplateView
from stylehome.apps.shop.models import Product

# Create your views here.
class ShopView(TemplateView):
    """
    Displays the shop main page
    """
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class ProductDetailView(TemplateView):
    """
    Displays the product detail page
    """
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        similar_products = Product.objects.filter(category_id=product.category_id).exclude(id=product.id)
        context['product'] = product
        context['similar_products'] = similar_products
        return context