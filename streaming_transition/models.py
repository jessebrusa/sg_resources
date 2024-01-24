from django.db import models


class Apartment(models.Model):
    apartment_number = models.IntegerField()
    building = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.apartment_number} {self.building}"
    

class Visit(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='visits')
    date = models.DateField()
    time = models.TimeField()
    technician = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    time_completed = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.apartment.apartment_number}{self.apartment.building[0]} - {self.date}"
    

class Device(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='devices')
    device_type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    built_in = models.CharField(max_length=255, null=True, blank=True, default=None)
    smart_device = models.CharField(max_length=255, null=True, blank=True)
    recommendation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.apartment.apartment_number}{self.apartment.building[0]} - {self.device_type}: {self.model}"