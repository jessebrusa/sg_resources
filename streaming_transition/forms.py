from django import forms
from .models import Device, Visit
from django.forms.widgets import DateInput, TimeInput


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type', 'model', 'built_in', 
                  'smart_device', 'recommendation']
        

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['date', 'time', 'comment']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
        }


class VisitHomeForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['apartment','date', 'time', 'comment']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
        }