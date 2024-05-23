from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from . import serializers
from rest_framework.permissions import AllowAny

# Create your views here.
class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [AllowAny]