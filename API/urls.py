from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, TransactionLogViewSet

router = DefaultRouter()
router.register("items", InventoryItemViewSet, basename="items")
router.register("logs", TransactionLogViewSet, basename="logs")

urlpatterns = [
    path("", include(router.urls)),
]
