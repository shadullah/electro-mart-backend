from rest_framework import serializers
from rest_framework import viewsets
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'