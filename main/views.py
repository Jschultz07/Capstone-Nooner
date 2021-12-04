from django.shortcuts import render
from django.http import HttpResponse
from .models import Urgency, Propertymanagement, Tenant, Item, Ticket, Troubleticket
from .forms import CreateNewTenants, CreateNewTickets, CreateNewProperty

# Create your views here.
def homes(response):
    ls = Item.objects.all()
    print(ls)
    return HttpResponse("<h1>TEST<h1>" %(ls))

def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    return HttpResponse("<h1>User Profile Info -rentals locations renter etc<h1>")

def tickets(response):
    return HttpResponse("<h1>All applicable trouble ticket info<h1>")

def tenants(response):
    return HttpResponse("<h1>Current user tenant info or all tenant info if manager<h1>")

def newTenants(response):
    form = CreateNewTenants(response.POST or None)
    if form.is_valid():
        form.save()
    return render(response, "main/newTenant.html", {"form":form})

def newProperty(response):
    form = CreateNewProperty(response.POST or None)
    if form.is_valid():
        form.save()
    return render(response, "main/newProperty.html", {"form":form})

def newTickets(response):
    form = CreateNewTickets(response.POST or None)
    if form.is_valid():
        form.save()
        print("Test")

    return render(response, "main/newTicket.html", {"form":form})
