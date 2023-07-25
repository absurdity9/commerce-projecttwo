from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django import forms
from .models import User
from .models import Items
from .models import Listing
from .forms import createForm

def index(request):
    #context ={
    #    "active_listings": Listing.item
    #}
    return render(request, "auctions/index.html", context)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createItems_and_Listing(data):
    title = data["title"]
    desc = data["desc"]
    floor_price = data["floor_price"]
    photo_url = data["photo_url"]
    date_end = data["date_end"]
    
    # create an item record
    item = Items.objects.create(title=title, desc=desc, floor_price=floor_price, photo_url=photo_url)
    
    listing = Listing.objects.create(item=item, date_end=date_end)
    
    return item, listing


def createListing(request):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            item, listing = createItems_and_Listing (form_data)
            return redirect("index")
        else:
            create_listing_form = createForm()
    else:
        return render(request, "auctions/createlisting.html", {"create_listing_form": createForm})
