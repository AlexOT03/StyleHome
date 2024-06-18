from django.urls import path
from stylehome.apps.home import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
