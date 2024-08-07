from django.urls import path
from stylehome.apps.shop import views

urlpatterns = [
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
]
