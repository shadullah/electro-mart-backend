from account.serializers import UserlistSerializer
from rest_framework import serializers
from rest_framework import viewsets
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        depth=1

    def to_representation(self, instance):
        data= super().to_representation(instance)
        data['user'] = UserlistSerializer(instance.user).data
        return data
    
    def validate(self, obj):
        obj['user'] = self.context['request'].user
        return obj 