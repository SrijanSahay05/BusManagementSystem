from django.contrib import admin
from .models import CustomUser, Passengers
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Passengers)