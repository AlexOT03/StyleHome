from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DeleteView, View
from stylehome.apps.cart.models import Carshop

# Create your views here.
class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Carshop.objects.all().prefetch_related('product_id')
        return context 
    

class DeleteCartView(DeleteView):
    
    def get(self, request,id):
        carshop = get_object_or_404(Carshop, id=id)
        carshop.delete()
        return redirect('cart')
