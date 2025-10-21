from django.shortcuts import render
from rest_framework import generics
from models import Inventory
from Serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from pagination import CustomPagination


class CreateView(generics.CreateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination


class DetailsView(generics.RetrieveAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination

class UpdateView(generics.UpdateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination


class DeleteView(generics.DestroyAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination

class ListView(generics.ListAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
