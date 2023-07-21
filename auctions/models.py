from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Items(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    floor_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_url = models.URLField
    
    