from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('spotter/', include('spotter.urls')),
    path('admin/', admin.site.urls),
]
