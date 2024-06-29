from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120)
    description= models.TextField(max_length=1200)
    price = models.IntegerField()
    condition=models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True,default="Watch", blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title