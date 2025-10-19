from django.shortcuts import render
from django.views import generic
from models import Inventory
from Serializers import InventorySerializer



class CreateView(generic.CreateView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer.serializers
    permission_classed= [iaAuthenticatedReadOnly]
