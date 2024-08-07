from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class State(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Municipality(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    WORK_CHOICES = (
        ('Cliente', 'Cliente'),
        ('Vendedor', 'Vendedor'),
        ('Proveedor', 'Proveedor'),
        ('Mantenimiento', 'Mantenimiento'),
    )
    
    type_user = models.CharField(choices=WORK_CHOICES, max_length=50, blank=True, default='Cliente')
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()], unique=True, max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[RegexValidator(r"^\+?1?\d{9,15}$")], blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profiles/')
    password = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardar
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class TypeWorker(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_work = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    salary = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"{self.type_work} (ID: {self.user_id.first_name})"
    
class Supplier(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.company} (ID: {self.user_id.first_name})"
    

class Supplies(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    tipo_insumo = models.CharField(max_length=100)
    costo = models.FloatField()
    unidades = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    
@receiver(post_save, sender=User)
def create_related_model(sender, instance, created, **kwargs):
    if created:
        if instance.type_user in ['Vendedor', 'Mantenimiento']:
            TypeWorker.objects.create(
                user_id=instance,
                type_work=instance.type_user,
                description='Descripción por defecto',
                salary=0.0
            )
        elif instance.type_user == 'Proveedor':
            Supplier.objects.create(
                user_id=instance,
                company='Nombre de la empresa por defecto',
                description='Descripción por defecto'
            )
