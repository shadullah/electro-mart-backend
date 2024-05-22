from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=40)
    description= models.TextField(max_length=120)
    price = models.IntegerField()
    condition=models.CharField(max_length=100)
    # category = models
    image = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title