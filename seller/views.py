from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Item
from . import serializers
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['title', 'description']