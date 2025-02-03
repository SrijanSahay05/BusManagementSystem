from django.db import models

# Create your models here.


class Day(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

class Date(models.Model):
    date = models.DateField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.date.strftime('%d/%m/%Y')
