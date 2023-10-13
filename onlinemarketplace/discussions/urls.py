from django.urls import path
from . import views

app_name='discussions'

urlpatterns = [
    path('',views.inbox, name='inbox'),
    path('<int:pk>', views.inside_convo, name='inside'),
    path('new/<int:item_pk>/', views.new_convo, name='new_convo'),

]
