from django.urls import path
from .views import StreamingTransitionHomeView, UncompleteView


urlpatterns = [
    path('', StreamingTransitionHomeView.as_view(), name='streaming-transition-home'),
    path('uncomplete/', UncompleteView.as_view(), name='uncomplete'),
]