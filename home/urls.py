from django.urls import path
from .views import *

urlpatterns = [
    path('reservations/',reservations,name = 'reservations'),
    path('contact/', contact, name = 'contact'),
]