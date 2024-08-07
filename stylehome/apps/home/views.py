from django.views.generic import TemplateView
from stylehome.apps.shop.models import Category

# Create your views here.
class HomeView(TemplateView):
    """ Home page view """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()[:4]
        context['categories'] = categories
        return context
