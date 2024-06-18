from django.urls import path
from stylehome.apps.about import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about')
]
