from django.contrib import admin

# Register your models here.
from .models import User, Items, Listing

admin.site.register(User)
admin.site.register(Items)
admin.site.register(Listing)