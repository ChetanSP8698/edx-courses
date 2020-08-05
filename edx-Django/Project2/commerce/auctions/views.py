from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, listings, bid, comments, Categories
from .forms import listing_form

def index(request):
    list = []
    entries = listings.objects.values_list()
    for item in entries:
        list.append(item[0:6])

    return render(request, "auctions/index.html", {
        "entries" : list
    })


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

@login_required(login_url='login')
def create_listing(request):
    if request.method == 'POST':
        form = listing_form(request.POST)
        if form.is_valid():
            obj = listings()
            obj.item_title = form.cleaned_data['title']
            obj.item_image = form.cleaned_data['image']
            obj.item_des = form.cleaned_data['descr']
            obj.item_price = form.cleaned_data['bid']
            obj.item_category = form.cleaned_data['category']
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = listing_form()
        
    return render(request, "auctions/listings.html", {
        'form' : form
    })

def item(request, id):
    obj = listings.objects.values_list()
    info = []
    for i in obj:
        if id == int(i[0]):
            it = i
    for item in it:
        info.append(item)
    
    for cat in Categories:
        if cat[0] == info[6]:
            info[6] = cat[1]
    return render(request, "auctions/item.html", {
        "item" : info
    })