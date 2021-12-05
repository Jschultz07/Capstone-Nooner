from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Urgency, Propertymanagement, Tenant, Item as Property , Ticket, Troubleticket
from .forms import CreateNewTenants, CreateNewTickets, CreateNewProperty

# Create your views here.
def homes(response):
    ls = Property.objects.all()  #returns all properties to the html file. 
    if response.method == "POST":
        if response.POST.get("new"):                        # if the user selects the new button 
            return HttpResponseRedirect("/new/property")    # redirect to the new property page and allow creation of property. 
       
        
        elif response.POST.get("delete"):                   # if they enter info in txt place and it is the address in list.
            text = response.POST.get("info")                # remove property from list. 
            for each in ls:                                 # NOTE removes all instances that the address matches. from list.  
                if text == each.address:
                    Property.objects.filter(address = text).delete()
        
            ls = Property.objects.all()                     # when completed refresh page with updated list. 
            return render(response, "main/properties.html", {"ls":ls})
        
        elif response.POST.get("save"):                                               # if not do something else. 
            for each in ls:
                cbinput = response.POST.get("c"+str(each.id))
                print(f"******** Response {cbinput}")
                if response.POST.get("c" + str(each.id)) == "rented":
                    each.rented = True
                else:
                    each.rented = False
                each.save()


    return render(response, "main/properties.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {})

def profile(request, pk):
    ls = Property.objects.get(id=pk)
    return render(request, "main/profile.html", {"ls":ls })

def tickets(response):
    ls = Ticket.objects.all()
    context = {
         "locations" : Property.objects.all(),
         "people" : Tenant.objects.all(),
         "ls" : Ticket.objects.all()
         }

    return render(response, "main/tickets.html", context)

def tenants(response):
     ls = Tenant.objects.all()
     context = {
         "locations" : Property.objects.all(),
         "ls" : Tenant.objects.all()
         }

     if response.method == "POST":
        if response.POST.get("new"):                        # if the user selects the new button 
            return HttpResponseRedirect("/new/tenants")      # redirect to the new property page and allow creation of property. 
       
        
        elif response.POST.get("delete"):                   # if they enter info in txt place and it is the address in list.
            text = response.POST.get("info")                # remove property from list. 
            for each in ls:                                 # NOTE removes all instances that the address matches. from list.  
                target = each.firstname + " " + each.lastname
                if target == text:
                    ID = each.id
                    Tenant.objects.filter(id = ID).delete()
        
            ls = Tenant.objects.all()                     # when completed refresh page with updated list. 
            return render(response, "main/tenants.html", {"ls":ls})
        
        
        elif response.POST.get("save"):                                               # if not do something else. 
            for each in ls:
                if response.POST.get("c" + str(each.id)) == "clicked":
                    each.pets = True
                else:
                    each.pets =  False
                each.save()




     return render(response, "main/tenants.html", context)

def newTenants(response):
    if response.method == "POST":
           print("\nnew property POST\n")
           form = CreateNewTenants(response.POST )#or None)    
           if form.is_valid():
               firstN = form.cleaned_data["firstname"]            # put in temp variables
               lastN = form.cleaned_data["lastname"]      
               jointN = form.cleaned_data["jointtenantname"]
               pt = form.cleaned_data["pets"]
               pr = form.cleaned_data["paidrent"]
               exp = form.cleaned_data["leaseexpdate"]
               PN = form.cleaned_data["phonenumber"]      
               EM = form.cleaned_data["email"]
               ad = form.cleaned_data["address"]
               


               # using temp variables creeate an instance of Object with values gleaned
               #
               new = Tenant(firstname = firstN, lastname = lastN, jointtenantname = jointN, pets = pt, paidrent = pr, leaseexpdate = exp, phonenumber = PN, email = EM, address = ad  ) 
               
               # save that input to object list. 
               new.save()

               return HttpResponseRedirect("/tenants")
    form = CreateNewTenants()
    if form.is_valid():
        form.save()
    return render(response, "main/newTenant.html", {"form":form})

def newProperty(response):
    if response.method == "POST":
           print("\nnew property POST\n")
           form = CreateNewProperty(response.POST )#or None)
           if form.is_valid():                              # if valid get the imput from form 
               ad = form.cleaned_data["address"]            # put in temp variables
               available = form.cleaned_data["rented"]      
               cost = form.cleaned_data["rentprice"]
               bed = form.cleaned_data["bedrooms"]
               bath = form.cleaned_data["bathrooms"]
               t = form.cleaned_data["tenant"]
                
               # using temp variables creeate an instance of Object with values gleaned
               #
               new = Property(address = ad,rented=available,bedrooms=bed,bathrooms=bath,tenant=t)
               
               # save that input to object list. 
               new.save()

               return HttpResponseRedirect("/homes")

    else:
       form = CreateNewProperty()
       if form.is_valid():
           form.save()
    return render(response, "main/newProperty.html", {"form":form})

#                #this line generates a blank form and passes it into the {} arguements for django to generate for us
#        #pass the form into the create.html as an arguement. 

def newTickets(response):
    form = CreateNewTickets(response.POST or None)
    if form.is_valid():
        form.save()
        print("Test")

    return render(response, "main/newTicket.html", {"form":form})




#To add/commit/push:

# in bash terminal (git) navigate to the file ( master)
# git add .
#git commit -m "some comment here"
#git push origin master
 #pw  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
 #this submits and saves files and assets to github and local git machine
 # !!!
