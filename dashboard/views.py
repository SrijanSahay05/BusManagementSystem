from django.shortcuts import render
from busmanagement.models import Route, Stop, Halt, Bus
from dashboard.models import Day, Date
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "dashboard/index.html")


def admin_dashboard(request):

    stops = Stop.objects.all()
    days = Day.objects.all()
    routes = Route.objects.all()

    if request.method == "POST":
        if "add_route" in request.POST:
            print("Incoming POST request for Route Addition")
            name = request.POST["routeName"]
            number = request.POST["routeNumber"]
            source_id = request.POST["source"]
            destination_id = request.POST["destination"]
            departure_time = request.POST["departureTime"]
            arrival_time = request.POST["arrivalTime"]
            journey_duration = request.POST["journeyDuration"]
            running_days_id = request.POST.getlist("runningDays") 
            # halts = request.POST.getlist("halts")
            source = Stop.objects.get(id=source_id)
            destination = Stop.objects.get(id=destination_id)
            running_days = Day.objects.filter(id__in=running_days_id)
            print(f"Name: {name}, number: {number}, source: {source}, destination: {destination}, departure_time: {departure_time}, arrival_time: {arrival_time}, journey_duration: {journey_duration}, running_days: {running_days}")

            try:
                route = Route.objects.create(name=name, number=number, source=source, destination=destination, departure_time=departure_time, arrival_time=arrival_time, journey_duration=journey_duration)
                route.running_days.set(running_days)
                route.save()
                print("Route created successfully")
                messages.success(request, "Route created successfully")
            except Exception as e:
                print(f"Error creating route: {e}")
                messages.error(request, f"Error creating route: {e}")
        if "add_halt" in request.POST:
            print("Incoming POST request for Halt Addition")
            route_id = request.POST["route"]
            stop_id = request.POST["stop"]
            arrival_time = request.POST["arrivalTime"]
            departure_time = request.POST["departureTime"]
            order = request.POST["haltNumber"]

            route = Route.objects.get(id=route_id)
            stop = Stop.objects.get(id=stop_id)
            print(f"Route: {route}, Stop: {stop}, Arrival Time: {arrival_time}, Departure Time: {departure_time}, Order: {order}")

            try:
                halt = Halt.objects.create(route=route, stop=stop, arrival_time=arrival_time, departure_time=departure_time, order=order)
                print("Halt created successfully")
                messages.success(request, "Halt created successfully")
            except Exception as e:
                print(f"Error creating halt: {e}")
                messages.error(request, f"Error creating halt: {e}")


                 

    context = {
        "stops": stops, 
        "days": days,
        "routes": routes,
    }
    return render(request, "dashboard/admin_dashboard.html", context=context)

