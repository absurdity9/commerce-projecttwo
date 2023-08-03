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
    path("listing/<int:itemid>", views.listing, name="listing"),
    path("close_listing/<int:item_id>", views.close_listing, name="close_listing"),
    path("add_watchlist/<int:item_id>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<int:item_id>", views.remove_watchlist, name="remove_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),
]
