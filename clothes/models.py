from django.db import models

# Create your models here.
class Clothes(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    sold = models.IntegerField(null=True)
    cover = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='clothes')

    def __str__(self):
        return f"{self.title}"
