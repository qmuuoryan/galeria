from django.db import models

# Create your models here.
def location(models.Model):
    location_name = models.CharField(max_length =30)

     def __str__(self):
            return self.location
    