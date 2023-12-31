import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from .forms import AddItemForm, EditItemForm

# create the detail of an item
def detail(request, pk):
    # to get this from the database
    item = get_object_or_404(Item, pk=pk)
    same_cat_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/detail.html',{'item': item,
                                                'related_items': same_cat_items})


def explore(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category',0)
    query = request.GET.get('query','')
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request, 'items/explore.html', {
        'items': items,
        'query' : query,
        'categories': categories,
        'category_id' : int(category_id)})


@login_required
def addNewItem(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = AddItemForm()
    return render(request, 'items/form.html', {
        'form': form,
        'title' : 'Add Item'
    })


@login_required
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def deleteItem(request, pk):
   item = get_object_or_404(Item, pk=pk, created_by=request.user)
   item.delete()
   return redirect('core:index')
