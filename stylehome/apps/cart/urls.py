from django.urls import path
from stylehome.apps.cart import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/delete/<int:id>/', views.DeleteCartView.as_view(), name='delete-cart'),
]
