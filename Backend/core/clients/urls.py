# clients/urls.py
from django.urls import path
from . import views
from .views import ClientSerializerAPIview

urlpatterns = [
    path('clients/', ClientSerializerAPIview.as_view()),
    path('clients/<int:pk>/', ClientSerializerAPIview.as_view()),
    path('clients/<int:pk>/update/', ClientSerializerAPIview.as_view()),    
    path('clients/<int:pk>/delete/', ClientSerializerAPIview.as_view()),
    path('clients/<int:pk>/update/', ClientSerializerAPIview.as_view()),
    path('clients/<int:pk>/retrieve/', ClientSerializerAPIview.as_view()),
]

