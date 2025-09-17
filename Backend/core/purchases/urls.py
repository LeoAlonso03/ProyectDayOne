from django.urls import path
from . import views
from .serializers import PurchaseSerializer


urlpatterns = [
    path('purchases/', views.PurchaseListCreateAPIView.as_view(), name='purchase-list'),
    path('purchases/<int:pk>/', views.PurchaseRetrieveUpdateDestroyAPIView.as_view(), name='purchase-detail'),
]
