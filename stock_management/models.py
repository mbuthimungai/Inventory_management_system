from django.db import models
# from item_management.models import Item
import uuid
class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey("item_management.Item", on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self):        
        return f"Stock of {self.item.name}"