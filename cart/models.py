from django.db import models

from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(null=True)
    quantity = models.PositiveIntegerField(default=1)
