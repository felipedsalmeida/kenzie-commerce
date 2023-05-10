from django.db import models
from rest_framework.fields import MinValueValidator


class ORDER_STATUS(models.TextChoices):
    PLACED = "Order Placed"
    PENDING = "In Progress"
    DELIVERED = "Delivered"


class Order(models.Model):
    buyer = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="orders"
    )
    status = models.CharField(
        choices=ORDER_STATUS.choices, default=ORDER_STATUS.PLACED
    )
    products = models.ManyToManyField(
        "products.Product",
        related_name="orders",
        through="Order_Products",
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Order_Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
