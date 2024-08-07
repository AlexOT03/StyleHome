from django.contrib import admin
from .models import Product, Category, Color, Material, Acabado
# Register your models here.
    
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Acabado)