from django.db import models
# from item_management.models import Item
import uuid
class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey("item_management.Item", on_delete=models.CASCADE, related_name="stocks")
    quantity = models.IntegerField()
    business = models.ForeignKey(
        "business_management.Business",  # Relación con el modelo Business
        on_delete=models.CASCADE,       # Si el negocio es eliminado, también se eliminan los stocks
        related_name="stocks"           # Permite acceder a los stocks desde el negocio
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"