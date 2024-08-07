from django.contrib import admin
from .models import State, Municipality, TypeWorker, User, Supplier, Supplies
# Register your models here.
    
admin.site.register(State)
admin.site.register(Municipality)
admin.site.register(User)
admin.site.register(TypeWorker)
admin.site.register(Supplier)
admin.site.register(Supplies)