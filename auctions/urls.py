from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createListing, name="createlisting"),
    path("categories", views.categories, name="categories"),
    path("category_detail/<str:cat_name>", views.category_detail, name="category_detail"),
    path("listing/<str:itemid>", views.listing, name="listing"),
    path("close_listing/<int:itemid>/", views.close_listing, name="close_listing")    
]
