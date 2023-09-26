from django.contrib import admin
from .models import Category, Item
# ask to showcase the Category table in the admin interface
admin.site.register(Category)
admin.site.register(Item)
