from django.urls import path
from stylehome.apps.service import views

urlpatterns = [
    path('service/', views.ServiceView.as_view() ,name='service')
]
