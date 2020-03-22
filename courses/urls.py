from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course', views.add_course, name='add_course'),
    path('remove_course', views.remove_course, name='remove_course'),
]
