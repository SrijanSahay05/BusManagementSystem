from django.shortcuts import render, redirect
from busmanagement.models import Route, Bus 
from dashboard.models import Date 
# Create your views here.

def generate_bus(request):
    routes = Route.objects.all()
    dates = Date.objects.all()
    for route in routes:
        for data in dates:
            if Bus.objects.filter(route=route, date=data).exists():
                print(f"Bus for {route} on {data} already exists")
                pass
            else:
                print(f"Creating bus for {route} on {data}")
                Bus.objects.create(route=route, date=data)

    return redirect("admin-dashboard")