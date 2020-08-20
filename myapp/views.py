from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    designer = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designer})

def introduce(request):
    return render(request, 'introduce.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()

        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id) 
    else:
        return render(request, 'new.html')

def update(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']    
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id) 
    else:
        return render(request, 'update.html', {'designer' : post})    