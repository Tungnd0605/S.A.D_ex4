from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    sold = models.IntegerField(null=True)
    cover = models.CharField(max_length=255)
    type = models.CharField(max_length=255,default='book')
    def __str__(self):
        return f"{self.title}"