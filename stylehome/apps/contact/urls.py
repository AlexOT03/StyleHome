from django.urls import path
from stylehome.apps.contact import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
]
