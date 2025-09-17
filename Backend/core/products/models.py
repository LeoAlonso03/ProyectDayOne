from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    uiid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):  
        return self.nombre_producto











