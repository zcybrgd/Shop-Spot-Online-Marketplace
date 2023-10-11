from django.db import models
from items.models import Item
from django.contrib.auth.models import User
class Discussion(models.Model):
    item = models.ForeignKey(Item, related_name='discussions', on_delete=models.CASCADE)
    engaging_users = models.ManyToManyField(User, related_name='discussions')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class Conversation(models.Model):
    conversation = models.ForeignKey(Discussion, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
