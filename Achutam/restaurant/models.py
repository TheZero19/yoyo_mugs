from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class MenuItemType(models.Model):
    menuItemTypeID = models.AutoField(primary_key = True)
    menuItemType = models.CharField(max_length=30)

    def __str__(self):
        return self.menuItemType


class MenuItem(models.Model):
    menuItemID = models.AutoField(primary_key = True)
    itemName = models.CharField(max_length=40)
    itemType = models.ForeignKey(MenuItemType, on_delete=models.CASCADE, null=True, default=None)
    itemPPU = models.IntegerField()

    def __str__(self):
        return self.itemName


class Order(models.Model):
    orderID = models.AutoField(primary_key = True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    isPending = models.BooleanField(default=True)