from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    seller = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="listed_products"
    )
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
