from django.contrib import admin
from .models import Route, Stop, Halt, Bus
# Register your models here.
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(Halt)
admin.site.register(Bus)