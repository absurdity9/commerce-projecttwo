from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime 

class User(AbstractUser):
    pass

class Items(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    floor_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_url = models.URLField(default='https://images.unsplash.com/photo-1626846116799-ad61f874f99d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2940&q=80')    
class Listing(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(default=datetime(2023, 12, 31, 0, 0, 0))