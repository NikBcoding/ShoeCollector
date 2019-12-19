from django.db import models
from django.urls import reverse

# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
        
    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})
