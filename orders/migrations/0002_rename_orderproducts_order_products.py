# Generated by Django 4.2.1 on 2023-05-05 17:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderProducts",
            new_name="Order_Products",
        ),
    ]
