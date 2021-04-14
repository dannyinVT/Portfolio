from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Main Home'),
    path('index', views.index, name='Bootstrap index')
]
