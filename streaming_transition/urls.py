from django.urls import path
from .views import LandingPageView, UserLoginView, UserLogoutView


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', UserLoginView.as_view(next_page='landing-page'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]