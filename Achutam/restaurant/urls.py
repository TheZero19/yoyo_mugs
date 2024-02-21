from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="restaurant-index"),
    path("menu/", views.menu, name= "restaurant-menu"),
    path("about/", views.about, name= "restaurant-about"),
]