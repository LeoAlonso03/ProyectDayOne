from dataclasses import fields
from django.db import models
import uuid


# Create your models here.

class Client(models.Model):
    uiid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_cliente, self.email, self.telefono, self.direccion











