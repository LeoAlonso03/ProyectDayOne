from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import ClientSerializer
from .models import Client

# Create your views here.
class ClientSerializerAPIview(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

