# Generated by Django 5.0 on 2024-05-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
