# Generated by Django 5.0 on 2024-05-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=120)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='seller/static/img/')),
            ],
        ),
    ]
