# Generated by Django 4.2.1 on 2023-05-08 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart_products",
            name="amount",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
