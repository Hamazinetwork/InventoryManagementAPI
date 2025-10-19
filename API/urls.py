from django.urls import path
from .views import (
    CreateView,
    DeleteView,
    DetailsView,
    UpdateView,
    ListView
)

urlpatterns=[
    path("Inventory/", CreateView.as_view(), name="create-list"),
    path("Inventory/", DeleteView.as_view(), name="delete-list"),
    path("Inventory/", DetailsView.as_view(), name="details-list"),
    path("Inventory/", UpdateView.as_view(), name="update-list"),
    path("Inventory/", ListView.as_view(), name="list"),
    
]