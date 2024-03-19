from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from checkout.models import Checkout
# Create your models here.

class Delivery(models.Model):
    order = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    shipment_vendor = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
