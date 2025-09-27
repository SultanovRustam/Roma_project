from django.shortcuts import render
from eras.models import Era

def home(request):
    eras = Era.objects.all().order_by('order')
    return render(request, 'timeline/home.html', {'eras': eras})
