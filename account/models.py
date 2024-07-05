# from typing import Iterable
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     USER_TYPE_CHOICES = [
#         ('Buyer', 'Buyer'),
#         ('Seller', 'Seller'),
#         ('Admin', 'Admin'),
#     ]

#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')

# class AdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.URLField(default="https://static.vecteezy.com/system/resources/thumbnails/005/129/844/small_2x/profile-user-icon-isolated-on-white-background-eps10-free-vector.jpg", null=True, blank=True)

#     def __str__(self) -> str:
#         return f'Admin - {self.user.username}'
    
#     def save(self, *args, **kwargs):
#         self.user.user_type = 'Admin'
#         self.user.save()
#         return super().save(*args **kwargs)
