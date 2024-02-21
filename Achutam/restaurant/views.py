from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItemType, MenuItem

# Create your views here.
def index(request):
    return render(request, "restaurant/index.html")

def menu(request):
    menu_item_types = MenuItemType.objects.all()
    menu_items = MenuItem.objects.all()
    return render(request, "restaurant/menu.html", {'menu_item_types': menu_item_types,
                'menu_items' : menu_items})

def about(request):
    return render(request, "restaurant/about.html")
