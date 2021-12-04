from django import forms
from django.forms import ModelForm
from .models import Ticket, Item as Property, Tenant,Urgency, Category


class CreateNewTickets(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticketno','date','issue','complete','notes','item','tenant','urgency']
    
class CreateNewTenants(forms.Form):
    firstname = forms.CharField(label = "First Name", max_length = 90)
    lastname = forms.CharField(label = "Last Name", max_length = 90)
    jointtenantname = forms.CharField(label = "Joint Tenant if applicable", max_length = 90, required = False)
    leaseexpdate = forms.CharField(label = "Lease Renewal Date", max_length = 30, required = False)
    phonenumber = forms.CharField(label = "Phone number", max_length = 15)
    email = forms.EmailField(label = "Email", max_length = 90)
    address = forms.CharField(label = "Current Address", max_length = 100)
    pets = forms.BooleanField(required = False)
    paidrent = forms.BooleanField(required = False, label = "Current rent and deposit paid?")

class CreateNewProperty(ModelForm):
    address = forms.CharField(label = "Address", max_length = 200)
    rented = forms.BooleanField(label= "Currently Rented", required = False)
    rentprice = forms.CharField(label = "Rent $", max_length = 10, required = False)
    bedrooms= forms.CharField(label = "Beds", max_length = 3)
    bathrooms= forms.CharField(label = "Baths", max_length = 3)
    class Meta:
        model = Property 
        fields = ['tenant'] 