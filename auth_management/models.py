from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AuthUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    identification_number = models.CharField(max_length=20, blank=False, unique=True, db_index=True)
    
    def __str__(self):
        return self.username + " - " + self.first_name + " " + self.last_name
