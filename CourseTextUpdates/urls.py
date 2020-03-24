from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='account')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('loops/', include(('loops.urls', 'loops'), namespace='loops')),
    path('admin/', admin.site.urls),
]
