from django.shortcuts import render
from rest_framework import generics
from models import Inventory
from Serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend

class CreateView(generics.CreateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price' ]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'Createdat']


class DetailsView(generics.RetrieveAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price' ]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'Createdat']

class UpdateView(generics.UpdateAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price' ]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'Createdat']


class DeleteView(generics.DestroyAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price' ]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'Createdat']

class ListView(generics.ListAPIView):
    queryset= Inventory.objects.all()
    seralizers_class=InventorySerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    pagination_class= CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price' ]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'Createdat']
