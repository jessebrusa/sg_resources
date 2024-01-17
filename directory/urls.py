from django.urls import path
from .views import Directory

urlpatterns = [
    path('', Directory.as_view(), name='directory'),
]