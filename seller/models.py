from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40)
    description= models.TextField(max_length=120)
    price = models.IntegerField()
    condition=models.CharField(max_length=100)
    # category = models
    image = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title