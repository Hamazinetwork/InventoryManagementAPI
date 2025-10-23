from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, TransactionLogViewSet

router = DefaultRouter()
router.register("items", InventoryItemViewSet, basename="items")
router.register("logs", TransactionLogViewSet, basename="logs")
from . import views_auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", include(router.urls)),
    path('logout/', views_auth.logout_view, name='logout'),
    path('login/', views_auth.login_view, name='login'),
    path('register/', views_auth.register_view, name='register'),
    path('dashboard/', views_auth.dashboard_view, name='dashboard'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
