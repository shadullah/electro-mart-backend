# Generated by Django 5.0 on 2024-05-22 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_item_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='img',
        ),
    ]
