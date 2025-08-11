from django.shortcuts import render
from django.config import settings

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {'restaurnat_name': settings.RESTAURANT_NAME , 'restaurant_phone' : settings.RESTAURANT_PHONE})


def about(request):
    return render(request, 'home/about.html', {'restaurant_name': settings.RESTAURANT_NAME})

def contact(request):
    info = {
        'name' : getattr(settings, 'RESTAURANT_NAME', 'My Restaurant'),
        'phone' : '+91 98765 43',
        'email' : 'info@example.com',
        'address' : '123 Food Street, AOnla, Barielly',
    }
    return render(request, 'home/contact.html', {'info': info})