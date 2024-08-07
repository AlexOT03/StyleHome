from django.urls import path
from stylehome.apps.client import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('post/', views.post, name='post'),
    path('register_user/', views.register, name='register_user'),
]
