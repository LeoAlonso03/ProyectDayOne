from django.db import models
import uuid


# Create your models here.

class Purchase(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente_uuid = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='compras')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField('products.Product', related_name='compras')  
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.uuid} - Total: ${self.total}"  # ✅ Devuelve string

        














