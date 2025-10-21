from django.shortcuts import render
from rest_framework import generics
from models import Inventory
from Serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CreateView(generics.CreateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]


class DetailsView(generics.RetrieveAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]

class UpdateView(generics.UpdateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]

class DeleteView(generics.DestroyAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]

class ListView(generics.ListAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
