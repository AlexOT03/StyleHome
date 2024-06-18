from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ServiceView(TemplateView):
    """
    View for service page
    """
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
