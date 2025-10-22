from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InventoryItem, TransactionLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class InventoryItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = InventoryItem
        fields = "__all__"

class TransactionLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = serializers.StringRelatedField()

    class Meta:
        model = TransactionLog
        fields = "__all__"
