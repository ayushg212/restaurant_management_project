from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('',menu_list, name = 'menu'),
    path('simple/', simple_menu, name= 'api_simple_menu'),
]