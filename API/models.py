from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="items_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="items_updated")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TransactionLog(models.Model):
    ACTION_CHOICES = [
        ("ADD", "Add"),
        ("UPDATE", "Update"),
        ("DELETE", "Delete"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    quantity_changed = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.item.name}"
