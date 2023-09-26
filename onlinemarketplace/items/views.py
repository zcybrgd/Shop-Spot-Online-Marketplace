from django.shortcuts import render, get_object_or_404
from .models import Item
# create the detail of an item

def detail(request, pk):
    # to get this from the database
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html',{'item': item})