# Generated by Django 4.2.1 on 2023-05-05 15:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "stock",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="listed_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
