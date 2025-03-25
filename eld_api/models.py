from django.db import models

# Create your models here.
from django.db import models

class Trip(models.Model):
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cycle_hours = models.FloatField()  # Total driving hours
    driver_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.driver_name} - {self.location}"

class ELDLog(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=50)  # e.g., "Driving", "Rest", "Off-Duty"
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.log_type} - {self.trip.driver_name}"