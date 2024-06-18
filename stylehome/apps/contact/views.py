from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    """
    Class based view for contact page
    """
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
