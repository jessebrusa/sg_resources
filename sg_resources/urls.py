from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streaming-transition/', include('streaming_transition.urls')),
    path('', include('directory.urls')),
]
