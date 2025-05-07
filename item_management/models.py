from django.db import models
# from category_management.models import Category
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey("category_management.Category", on_delete=models.CASCADE, related_name="items")
    business = models.ForeignKey(
        "business_management.Business",  # Relación con el modelo Business
        on_delete=models.CASCADE,       # Si el negocio es eliminado, también se eliminan los items
        related_name="items"            # Permite acceder a los items desde el negocio
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name