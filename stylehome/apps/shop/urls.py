from django.urls import path, re_path
from stylehome.apps.shop import views

urlpatterns = [
    path('shop/product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    re_path(r'^shop/(?P<category_id>.*)?$', views.ShopView.as_view(), name='shop_with_category'),
]
