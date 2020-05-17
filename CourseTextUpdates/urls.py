from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('courses.urls', 'courses'), namespace='courses')),
    path('admin/', admin.site.urls),
]
