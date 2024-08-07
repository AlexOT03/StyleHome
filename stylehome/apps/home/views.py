from django.views.generic import TemplateView
from stylehome.apps.shop.models import Category

# Create your views here.
class HomeView(TemplateView):
    """ Home page view """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_big = Category.objects.all().order_by('name')[4:]
        categories_small = Category.objects.all().order_by('name')[:4]
        context['categories_big'] = categories_big
        context['categories_small'] = categories_small
        return context
