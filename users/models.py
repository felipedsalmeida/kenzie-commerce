from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class USER_TYPE(models.TextChoices):
    ADMIN = "Admin"
    SELLER = "Seller"
    CUSTOMER = "Customer"


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    type = models.CharField(
        max_length=20, choices=USER_TYPE.choices, default=USER_TYPE.SELLER
    )
    address = models.OneToOneField("addresses.Address", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
