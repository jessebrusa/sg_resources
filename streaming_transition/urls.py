from django.urls import path
from .views import *


urlpatterns = [
    path('', StreamingTransitionHomeView.as_view(), name='streaming-transition-home'),
    path('uncomplete/', UncompleteView.as_view(), name='uncomplete'),
    path('complete/', CompleteView.as_view(), name='complete'),
    path('upcoming/', UpcomingVisitsView.as_view(), name='upcoming'),

    path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='apartment'),

    path('device-form/<int:pk>/', DeviceCreateView.as_view(), name='device-form'),
    path('visit-form/<int:pk>/', VisitCreateView.as_view(), name='visit-form'),
    path('visit-home-form/', VisitHomeCreateView.as_view(), name='visit-home-form'),

    path('complete-apartment-check/<int:pk>/', CompleteApartmentCheckView.as_view(), name='complete-apartment-check'),
    path('not-complete-apartment-check/<int:pk>/', NotCompleteApartmentCheckView.as_view(), name='not-complete-apartment-check'),
    path('complete-visit-check/<int:pk>/', CompleteVisitCheckView.as_view(), name='complete-visit-check'),
]