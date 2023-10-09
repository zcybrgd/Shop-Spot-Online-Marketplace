from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import AddItemForm, EditItemForm
# create the detail of an items
def detail(request, pk):
    # to get this from the database
    item = get_object_or_404(Item, pk=pk)
    same_cat_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/detail.html',{'item': item,
                                                'related_items': same_cat_items})

@login_required
def addNewItem(request):
    if request.method == 'POST':
        newItemForm = AddItemForm(request.POST, request.FILES)
        if newItemForm.is_valid():
            item = newItemForm.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:detail', pk=item.id)
    else:
        newItemForm = AddItemForm()
    return render(request, 'items/form.html', {
        'form': newItemForm,
        'title' : 'Add Item'
    })



@login_required
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        editItemForm = EditItemForm(request.POST, request.FILES, instance=item)
        if editItemForm.is_valid():
            # i added this
            item = editItemForm.save()
            # right above
            item.save()
            editItemForm.save()
            return redirect('items:detail', pk=item.id)
    else:
        editItemForm = EditItemForm(instance=item)
    return render(request, 'items/form.html', {
        'form': editItemForm,
        'title' : 'Edit Item'
    })

@login_required
def deleteItem(request, pk):
   item = get_object_or_404(Item, pk=pk, created_by=request.user)
   item.delete()
   return redirect('core:index')
