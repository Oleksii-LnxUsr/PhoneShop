from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=35, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'users'

        