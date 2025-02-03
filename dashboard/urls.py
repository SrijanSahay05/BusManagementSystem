from django.urls import path
from . import views
from busmanagement.views import generate_bus
urlpatterns = [
    path('', views.index, name='index'),
    path('generate-bus/', generate_bus, name='generate-bus'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
]