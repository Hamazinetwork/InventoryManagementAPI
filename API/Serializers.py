from rest_framework import serializers
from .models import InventoryItem, TransactionLog
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class InventoryItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'created_by', 'created_at', 'updated_at']


class TransactionLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = InventoryItemSerializer(read_only=True)

    class Meta:
        model = TransactionLog
        fields = ['id', 'user', 'item', 'action', 'quantity_changed', 'timestamp']
