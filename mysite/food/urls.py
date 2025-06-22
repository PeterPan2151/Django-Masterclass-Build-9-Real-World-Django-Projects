from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'), 
    path('items/', views.items, name='items')
]
