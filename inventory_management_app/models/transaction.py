import uuid
from django.db import models
from .item import Item

# Assuming the Item model is already defined as previously discussed
# from your_app_name.models import Item

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
    ]

    transactionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transactions')
    quantity = models.PositiveIntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    # customerId = models.CharField(max_length=100, blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.transaction_type.title()} on {self.date.strftime('%Y-%m-%d')}"
