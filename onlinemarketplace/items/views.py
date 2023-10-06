from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import AddItemForm
# create the detail of an items
def detail(request, pk):
    # to get this from the database
    item = get_object_or_404(Item, pk=pk)
    same_cat_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/detail.html',{'item': item,
                                                'related_items': same_cat_items})

@login_required
def addNewItem(request):
    newItemForm = AddItemForm()
    return render(request, 'items/form.html', {
        'form': newItemForm,
        'title' : 'Add Item'
    })