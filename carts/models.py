from django.db import models
from rest_framework.fields import MinValueValidator


class Cart(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    products = models.ManyToManyField(
        "products.Product",
        related_name="carts",
        through="Cart_Products",
    )


class Cart_Products(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    amount = models.IntegerField(validators=[MinValueValidator(1)])
