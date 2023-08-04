from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime 

class User(AbstractUser):
    pass
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=300)
    def __str__(self):
        return self.category

class Items(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    floor_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_url = models.URLField(default='https://images.unsplash.com/photo-1626846116799-ad61f874f99d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2940&q=80')    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    
    def get_user_id(self):
        return self.owner_id.id
    
    def __str__(self):
        return self.title

class Listing(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(default=datetime(2023, 12, 31, 0, 0, 0))
    highestbid = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return self.item.title

class Comments(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=244)
    item_id = models.ForeignKey(Items,on_delete=models.CASCADE, default="1")
    
    def __str__(self):
        return self.detail
    
class Watchlist(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    listingid = models.ManyToManyField(Listing)
    def __str__(self):
        return self.userid

class Bids(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    listingid = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=0)
    datecreated = models.DateTimeField(auto_now=True)