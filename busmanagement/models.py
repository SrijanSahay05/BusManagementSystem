from django.db import models
from dashboard.models import Day, Date


class Stop(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name}:{self.code}"

class Halt(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, blank=True, null=True)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    order = models.IntegerField(help_text="Order of stop in the route")

    class Meta:
        unique_together = ['stop', 'route', 'order']

    def __str__(self):
        return f"{self.stop}:{self.order} on {self.route} route"

class Route(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.IntegerField(unique=True)
    source = models.ForeignKey(Stop, related_name='source_routes', on_delete=models.CASCADE, blank=True, null=True)
    destination = models.ForeignKey(Stop, related_name='destination_routes', on_delete=models.CASCADE, blank=True, null=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    journey_duration = models.IntegerField(help_text="in minutes")
    halts = models.ManyToManyField(Halt, related_name='route_halts')
    running_days = models.ManyToManyField(Day)

    def __str__(self):
        return f"{self.name}:{self.number}"
    
class Bus(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.route} on {self.date}"
    
class SeatCategory(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.name}:{self.price}"
    
class Seat(models.Model):
    number = models.IntegerField()
    category = models.ForeignKey(SeatCategory, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.number} in {self.bus} of category {self.category}"

