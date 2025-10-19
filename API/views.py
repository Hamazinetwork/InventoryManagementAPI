from django.shortcuts import render
from rest_framework import generics
from models import Inventory
from Serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class CreateView(generics.CreateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]

class DetailsView(generics.RetrieveAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]

class UpdateView(generics.UpdateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]

class ListView(generics.ListAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
