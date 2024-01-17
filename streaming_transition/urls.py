from django.urls import path
from .views import StreamingTransitionHomeView


urlpatterns = [
    path('', StreamingTransitionHomeView.as_view(), name='streaming-transition-home'),
]