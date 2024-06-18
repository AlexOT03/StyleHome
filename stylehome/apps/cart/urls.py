from django.urls import path
from stylehome.apps.cart import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
]
