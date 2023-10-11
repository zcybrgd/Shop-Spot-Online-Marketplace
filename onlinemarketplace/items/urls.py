from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('',views.explore, name='explore'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/',views.addNewItem, name='new_item'),
    path('<int:pk>/edit', views.editItem, name='edit_item'),
    path('<int:pk>/delete', views.deleteItem, name='delete'),
]