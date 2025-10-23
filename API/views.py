from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InventoryItem, TransactionLog
from .serializers import InventoryItemSerializer, TransactionLogSerializer
from .pagination import CustomPagination

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all().order_by("-updated_at")
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class=CustomPagination

    def perform_create(self, serializer):
        item = serializer.save(created_by=self.request.user, updated_by=self.request.user)
        TransactionLog.objects.create(
            user=self.request.user,
            item=item,
            action="ADD",
            details=f"Created item {item.name}"
        )

    def perform_update(self, serializer):
        item = serializer.save(updated_by=self.request.user)
        TransactionLog.objects.create(
            user=self.request.user,
            item=item,
            action="UPDATE",
            details=f"Updated item {item.name}"
        )

    def perform_destroy(self, instance):
        TransactionLog.objects.create(
            user=self.request.user,
            item=instance,
            action="DELETE",
            details=f"Deleted item {instance.name}"
        )
        instance.delete()

    @action(detail=False, methods=["get"])
    def levels(self, request):
        """View current inventory levels"""
        items = InventoryItem.objects.all()
        data = [
            {"item": item.name, "quantity": item.quantity}
            for item in items
        ]
        return Response(data)


class TransactionLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransactionLog.objects.all().order_by("-timestamp")
    serializer_class = TransactionLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class=CustomPagination
