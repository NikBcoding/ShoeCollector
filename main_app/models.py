from django.db import models
from django.urls import reverse

TIME = (
    ('8', '8:00am'),
    ('9', '9:00am'),
    ('10', '10:00am'),
    ('11', '11:00am'),
    ('12', '12:00pm'),
    ('1', '1:00pm'),
    ('2', '2:00pm'),
    ('3', '3:00pm'),
    ('4', '4:00pm'),
    ('5', '5:00pm')
)


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


class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    time = models.CharField(
        max_length=1,
        choices=TIME,
    )

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
