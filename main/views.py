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

    return HttpResponse("<h1>All applicable trouble ticket info<h1>")

def tenants(response):
    return HttpResponse("<h1>Current user tenant info or all tenant info if manager<h1>")

def newTenants(response):
    form = CreateNewTenants(response.POST or None)
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
