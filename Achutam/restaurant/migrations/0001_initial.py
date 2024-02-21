# Generated by Django 5.0.2 on 2024-02-21 00:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('menuItemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=40)),
                ('itemPPU', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(to='restaurant.menuitem')),
            ],
        ),
    ]