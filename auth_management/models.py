from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AuthUser(AbstractUser):
    class UserType(models.TextChoices):
        CLIENT = 'CLIENT', _('Client')
        WORKER = 'WORKER', _('Worker')
        SUPERADMIN = 'SUPERADMIN', _('Superadmin')

    phone = models.CharField(max_length=15, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    identification_number = models.CharField(max_length=20, blank=False, unique=True, db_index=True)
    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.CLIENT,
    )
    client = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        limit_choices_to={'user_type': UserType.CLIENT},
        related_name='workers'
    )
    business = models.ForeignKey(
        "business_management.Business",  # Reemplaza "yourapp" por el nombre real de la app que contiene el modelo Business
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers"
    ) 


    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name} ({self.get_user_type_display()})"
