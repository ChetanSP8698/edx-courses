from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, listings, bid, comments, Categories, watch_list
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
    watlist = watch_list.objects.values_list()
    info = []
    for i in obj:
        if id == int(i[0]):
            it = i
    for item in it:
        info.append(item)
    
    for cat in Categories:
        if cat[0] == info[6]:
            info[6] = cat[1]
    flag = 0
    for i in watlist:
        if id in i:
            flag = 1
    
    if flag == 1:
        return render(request, "auctions/item.html", {
            "item" : info,
            "flag" : 'no'
        })
    else:
        return render(request, "auctions/item.html", {
            "item" : info,
            "flag" : 'yes'
        })


@login_required(login_url='login')
def watchlist(request, val):
    watlist = watch_list.objects.values_list()
    obj = listings.objects.values_list()
    wl = []
    for i in watlist:
        wl.append(i[1])
    info = []
    for v in obj:
        for t in wl:
            if t == v[0]:
                info.append(v)
    
    if val == 0:
        return render(request, "auctions/watchlist.html", {
            "entries" : info
        })
    
    elif request.method == 'POST':
        obj = watch_list()
        obj.watch_list_item = listings.objects.get(item_id=val)
        obj.save()
        return HttpResponseRedirect("/")
    
    elif request.method == 'GET':
        inst = watch_list.objects.filter(watch_list_item=val)
        inst.delete()
        return HttpResponseRedirect("/")
    
    else:
        return render(request, "auctions/watchlist.html", {
            "entries" : wl
        })

def categories(request):
    user = watch_list.objects.values_list()
    return render(request, "auctions/categories.html", {
        "entries" : user
    })

@login_required(login_url='login')
def do_bid(request):
    if request.method == "POST":
        done_bid = request.POST["Bid"]
        obj = bid.objects.values_list(flat=True)
        
        
        return render(request, "auctions/bid.html", {
            "val" : obj,
            "bid" : done_bid
        })
