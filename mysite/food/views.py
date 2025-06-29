from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
# new
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

def items(request):
    return HttpResponse('This is an item view')

def detail(request, item_id):
    return HttpResponse('This is item no/id: ' % item_id)
