from django.urls import path
from stylehome.apps.client import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]
