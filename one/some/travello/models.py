from django.db import models

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    price = models.IntegerField()

    
    