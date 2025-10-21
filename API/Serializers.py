from rest_framework import serializers
from models import quantity, description, createdat, updatedat, name, price
from models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Inventory
        field=[id, quantity,description, createdat, updatedat,name, price]

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Enter atleast 5 characters")
        return data