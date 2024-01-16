from django.db import models

class Apartment(models.Model):
    apartment_number = models.AutoField(primary_key=True)
    building = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)


class Device(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='devices')
    device_type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    smart_device = models.CharField(max_length=255, null=True, blank=True)