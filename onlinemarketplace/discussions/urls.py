from django.urls import path
from . import views

app_name='discussions'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_convo, name='new_convo'),

]
