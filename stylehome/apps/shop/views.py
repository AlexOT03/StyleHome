from django.shortcuts import render
from django.views.generic import TemplateView
from stylehome.apps.shop.models import Product, Color, Category

# Create your views here.
class ShopView(TemplateView):
    """
    Displays the shop main page
    """
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the optional 'category' parameter from kwargs
        category_id = kwargs.get('category_id', None)
        if category_id:
            products = Product.objects.filter(category_id=category_id)
            colors = Color.objects.all()
            categories = Category.objects.all()
            context['selected_category'] = categories.get(id=category_id)
        else:
            products = Product.objects.all()
            colors = Color.objects.all()
            categories = Category.objects.all()
        

        context['colors'] = colors
        context['categories'] = categories
        context['products'] = products # Add category to the context

        return context


class ProductDetailView(TemplateView):
    """
    Displays the product detail page
    """
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['similar_products'] = Product.objects.filter(category_id=product.category_id).exclude(id=product.id)
        context['product'] = product
        return context