from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignUp

def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
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

