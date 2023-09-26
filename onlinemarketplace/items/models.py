from django.db import models
from django.contrib.auth.models import User

# creating a new database model

class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='itemImages', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # so all the items of this user can be showed, and whenever the user is deleted, the items get automatically deleted
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('image',)
    def __str__(self):
        return self.name