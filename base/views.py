from django.shortcuts import render, redirect
from .models import Category, Image, Location
from .forms import ImageForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.search_image(category=q) or Image.filter_by_location(location=q)

    context = {'images':images}
    return render(request, 'base/home.html', context)

def add_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form,'categories':categories, 'locations':locations }
    return render(request, 'base/image_form.html', context)

def delete_image(request, pk):
    image = Image.objects.get(id=pk)
    
    if request.method == 'POST':
        image.delete_image()
        return redirect('home')

    context = {'obj': image }
    return render(request, 'base/delete.html', context)

def update_image(request, pk):
    categories = Category.objects.all()
    locations = Location.objects.all()

    image = Image.update_image(pk)
    form = ImageForm(instance=image)
    if request.method == "POST":
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form, 'categories':categories, 'locations':locations }
    return render(request, 'base/image_form.html', context)

