from django.urls import path
from .views import (
    CreateView,
    ListView,
    UpdateView,
    DetailsView,
    DeleteView
)

urlpatterns=[
    path("inventory/", CreateView.as_view(), name="create-view"),
    path("inventory/", ListView.as_view(), name="list-view"),
    path("inventory/", DetailsView.as_view(), name="details-view"),
    path("inventory/", UpdateView.as_view(), name="update-view"),
    path("inventory/", DeleteView.as_view(), name="delete-view"),
]