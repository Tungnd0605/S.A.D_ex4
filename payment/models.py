from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from checkout.models import Checkout
# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_details = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment for Order ID: {self.order.id}"

