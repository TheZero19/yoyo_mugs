from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "restaurant/index.html")

def menu(request):
    return render(request, "restaurant/menu.html")