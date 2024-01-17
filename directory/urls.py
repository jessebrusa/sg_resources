from django.urls import path
from .views import Directory, UserLoginView, UserLogoutView


urlpatterns = [
    path('', Directory.as_view(), name='directory'),

    path('login/', UserLoginView.as_view(next_page='directory'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]