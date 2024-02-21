from django.contrib import admin
from .models import MenuItem, Order, MenuItemType

# Register your models here.
admin.site.register(MenuItemType)
admin.site.register(MenuItem)
admin.site.register(Order)