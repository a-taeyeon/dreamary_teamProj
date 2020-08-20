from django.shortcuts import render
from .models import Designer

# Create your views here.
def home(request):
    designer = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designer})

def introduce(request):
    return render(request, 'introduce.html')