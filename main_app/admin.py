from django.contrib import admin
from .models import Car, Maintenance, Option

# Register your models here.

admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Option)

