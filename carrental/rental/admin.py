from django.contrib import admin
from .models import Car
from .models import Equipment
# Register your models here.
admin.site.register(Car)
admin.site.register(Equipment)