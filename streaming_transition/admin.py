from django.contrib import admin
from .models import Apartment, Device, Visit

admin.site.register(Apartment)
admin.site.register(Device)
admin.site.register(Visit)