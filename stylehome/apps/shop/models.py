from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='categories/')
    
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Acabado(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product (models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    acabado_id = models.ForeignKey(Acabado, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.FloatField(default=0.0)
    image = models.ImageField(blank=True, null = True,upload_to='products/')
    measurements = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
