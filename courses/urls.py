from django.urls import path

from . import views

urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('', views.index, name='index'),
    path('create_account', views.create_account, name='create_account'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('add_course', views.add_course, name='add_course'),
    path('remove_course', views.remove_course, name='remove_course'),
    path('sign_out', views.sign_out, name='sign_out')
]
