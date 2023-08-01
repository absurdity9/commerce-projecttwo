from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django import forms
from .models import User, Items, Category, Comments
from .models import Listing
from .forms import createForm, commentsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#Get listing info
def listing_list():
    listings = Listing.objects.all()
    return listings

def index(request):
    username = request.session.get('username')
    active_listings = Listing.objects.filter(date_end__gt=timezone.now())
    context = {
        "active_listings": active_listings
    }
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
            request.session['username']=username
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
    category = data["category"]
    # create records
    category = Category.objects.create(category=category)
    item = Items.objects.create(title=title, desc=desc, floor_price=floor_price, photo_url=photo_url, category=category)
    listing = Listing.objects.create(item=item, date_end=date_end)
    
    return category, item, listing

def createListing(request):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            category, item, listing = createItems_and_Listing (form_data)
            return redirect("index")
        else:
            print("Error posting")
            return render(request, "auctions/createlisting.html", {"create_listing_form": createForm})
    else:
        return render(request, "auctions/createlisting.html", {"create_listing_form": createForm})

def categories(request):
    categories = Category.objects.order_by().values('category').distinct()
    print(categories)
    context = {
        "categories": categories
    }
    return render(request, "auctions/categories.html", context)

def category_detail(request, cat_name):

    items = Items.objects.filter(category__category=cat_name)

    active_items = items.filter(listing__date_end__gt=timezone.now())

    active_listings = Listing.objects.filter(item__in=active_items)

    context = {
        'active_listings': active_listings,
        'category_name': cat_name,
    }
    return render(request, 'auctions/category_detail.html', context)

def listing(request, itemid):
    try:
        listing = Listing.objects.get(item_id=itemid)
        comments = Comments.objects.filter(item_id_id=itemid)
    except Listing.DoesNotExist:
        listing = None
        comments = None

    if request.method == "POST":
        form = commentsForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            comment = Comments.objects.create(
                detail=form_data['detail'],
                item_id_id=itemid,
                userid_id=request.user.id,
                date_created=timezone.now()
            )
            comment.save()
            return redirect("listing", itemid=itemid)
        else:
            print("Error posting")
            return render(request, "auctions/listing.html", {"create_comments_form": commentsForm})
    else:
        context ={
            'listing': listing,
            'comments': comments,
            "create_comments_form": commentsForm,
            }
        return render(request, "auctions/listing.html", context)

def close_listing(request, item_id):
    if request.method == "POST":
        item = Listing.objects.get(item_id=item_id)
        item.date_end = timezone.now()
        item.save()
        print(item.item.title)
        return render(request, "auctions/close_listing.html", {"item": item})
    else:
        print("Not a request")
        return HttpResponse("Form is not valid.")