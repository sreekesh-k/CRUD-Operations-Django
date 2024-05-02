from django.db import models

# Create your models here.

class ItemsInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()