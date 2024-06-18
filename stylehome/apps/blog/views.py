from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BlogView(TemplateView):
    """
    Blog View
    """
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
