from django.shortcuts import render
from django.config import settings

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {'restaurnat_name': settings.RESTAURANT_NAME})