from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignUp
from PIL import Image

def get_image_size(item):
    if item.image:
        img = Image.open(item.image.path)
        return img.size[0] * img.size[1]
    else:
        return 0

def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    sorted_items = sorted(items, key=get_image_size, reverse=True)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': sorted_items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)

        if form.is_valid():
            form.save()
            return redirect('core/login.html')
    else:
        form = SignUp()
    return render(request, 'core/signup.html', {
        'form': form
    })