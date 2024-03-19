from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"