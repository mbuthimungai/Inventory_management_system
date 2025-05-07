from django.db import models
import uuid
from business_management.models import Business

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.TextField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='categories')  # Relación con Business
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name