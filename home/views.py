from django.shortcuts import render
from django.config import settings
from .models import Feedback, MenuItem

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

def resvervations(request):
    return render(request, 'home/reservations.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        email = request.POST.get('email','').strip()
        comments = request.POST.get('comments','').strip()
        if comments:
            Feedback.objects.create(name = name , email = email, comments = comments)
            return redirect('feedback_thanks')
        return render(request, 'home/feedback.html')
    return render(request, 'home/feedback.html')

def feedback_thanks(request):
    return render(request, 'home/feedback_thanks.html')


def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html',{'items': items})