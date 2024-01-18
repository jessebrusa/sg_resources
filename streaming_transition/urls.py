from django.urls import path
from .views import *


urlpatterns = [
    path('', StreamingTransitionHomeView.as_view(), name='streaming-transition-home'),
    path('uncomplete/', UncompleteView.as_view(), name='uncomplete'),
    path('complete/', CompleteView.as_view(), name='complete'),

    path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),

    path('complete-apartment-check/<int:pk>/', CompleteApartmentCheckView.as_view(), name='complete-apartment-check'),
    path('not-complete-apartment-check/<int:pk>/', NotCompleteApartmentCheckView.as_view(), name='not-complete-apartment-check'),
]