from django.db import models


###################################################################################
## Models without fk
class State(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

class TypeWorker(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    salary = models.IntegerField()

class Color(models.Model):
    name = models.CharField(max_length=50)

class Finished(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='categories/')





###################################################################################
## Models whit fk
class Municipality(models.Model):
    cve_state = models.ForeignKey(State, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    finished = models.ForeignKey(Finished,on_delete = models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField()
    image = models.ImageField(blank=True, null = True,upload_to='products/')
    large = models.IntegerField()
    tall = models.IntegerField()

class Person (models.Model):
    type_worker = models.ForeignKey(TypeWorker,on_delete=models.PROTECT)
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    pathern = models.CharField(max_length=50)
    mathern = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    direction = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True,upload_to='profiles/')

class Order (models.Model):
    cve_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cve_customer = models.ForeignKey(Person, on_delete=models.PROTECT)
    units = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150)

class Carshop (models.Model):
    cve_customer = models.ForeignKey(Person, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now_add=True)

class Detail_Carsop_Order(models.Model):
    cve_order = models.ManyToManyField(Order, on_delete=models.PROTECT)
    cve_carshop = models.ManyToManyField(Carshop, on_delete=models.PROTECT)