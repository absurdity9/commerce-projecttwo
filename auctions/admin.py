from django.contrib import admin

# Register your models here.
from .models import User, Items, Listing, Category, Comments

admin.site.register(User)
admin.site.register(Items)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Comments)