from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categorys.as_view(), name="category")
]
