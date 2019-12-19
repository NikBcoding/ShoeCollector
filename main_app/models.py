from django.db import models

# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
        
    def __str__(self):
        return f"{self.brand} ({self.id})"