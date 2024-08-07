from django.db import models
from stylehome.apps.shop.models import Product
from stylehome.apps.client.models import User

class Carshop (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()
    
    def __str__(self):
        return f"Carshop {self.id}"
    
class Order (models.Model):
    carshop_id = models.ForeignKey(Carshop, on_delete=models.CASCADE)
    units = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return f"Order {self.id}"