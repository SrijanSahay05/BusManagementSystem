from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta
from .models import Day, Date

@receiver(post_save, sender=Day)
def create_dates(sender, instance, created, **kwargs):
    if created:
        for i in range(0, 90, 7):
            date = datetime.now().date() + timedelta(days=i)
            day = instance
            if not Date.objects.filter(date=date, day=day).exists():
                Date.objects.create(date=date, day=day)
                print(f"Created date for {day} on {date}")
            else:
                print(f"Date for {day} on {date} already exists")
