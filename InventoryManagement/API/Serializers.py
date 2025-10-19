from rest_framework import serializers
from models import quantity, description, createdat, updatedat, name, price

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MyModal
        field=[id, quantity,description, createdat, updatedat,name, price]