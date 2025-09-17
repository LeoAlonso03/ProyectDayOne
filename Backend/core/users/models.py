from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    uiid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):  
        return self.nombre_usuario

class Rol(models.Model):
    uiid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_rol = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_rol




