from django.db import models
import uuid

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=40, blank=False)
    email = models.EmailField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    