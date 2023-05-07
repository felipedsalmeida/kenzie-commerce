from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField()
    number = models.CharField()
    zip_code = models.IntegerField()
    city = models.CharField()
    state = models.CharField(max_length=2)
