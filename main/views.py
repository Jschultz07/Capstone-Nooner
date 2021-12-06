from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Urgency, Propertymanagement, Tenant, Item as Property , Ticket, Troubleticket, Category
from .forms import CreateNewTenants, CreateNewTickets, CreateNewProperty
from django.core.mail import send_mail
# Create your views here.
def homes(response):
    context = {
        "ls" : Property.objects.all(),
        "people" : Tenant.objects.all(),
        "user" : response.user
        }
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
              #  print(f"******** Response {cbinput}")
                if response.POST.get("c" + str(each.id)) == "rented":
                    each.rented = True
                else:
                    each.rented = False
                each.save()
    return render(response, "main/properties.html", context)

def home(response):
    return render(response, "main/home.html", {})

def profile(request):
    user = response.user
    ls = Property.objects.all()
    return render(request, "main/profile.html", {"ls":ls })

def tickets(response):
    U = response.user                                    # gives us active user
    ls = Ticket.objects.all()                 # gives us list of tenants belonging to user
    T = Tenant.objects.filter(user = U)

    if response.method == "POST":
       if response.POST.get("new"):
           print("awesome")
           return HttpResponseRedirect("/new/tickets")
        
       elif response.POST.get("save"):       # if not do something else. 
           
           for ticket in ls:
                print(f"ls = {ls}")
                if response.POST.get("c" + str(ticket.ticketno)) == "clicked":
                    ticket.complete = True
                else:                       # only management can remove pets from status.
                    ticket.complete = False
                ticket.save()
           return HttpResponseRedirect("/tickets")
           
    else:
       context = {
             "locations" : Property.objects.all(),
             "people" : Tenant.objects.all(),
             "ls" : Ticket.objects.all(),
         
             "user":U
             }
       if U.id > 3:
           queryset =list( Property.objects.none())
           for each in T:
               local = Property.objects.filter(tenant = each)
               queryset.append(list(local))
           
           peop = Tenant.objects.filter(user = U)
           print(f"  user***********{U}")
           print(f"  List of Tickets belonging to user ***********{ls}")
           print(f"  List of Tenants belonging to user***********{peop}")
           print(f"  List of Property ***********{queryset}")
           context = {
             "locations" : queryset,
             "people" : peop,
             "ls" : ls,
         
             "user":U
             }  
           
    return render(response, "main/tickets.html", context)

def tenants(response):
     user = response.user
     print(user)
     ls = Tenant.objects.all()
     context = {
         "locations" : Property.objects.all(),
         "ls" : Tenant.objects.all(),
         "user" : user
         }
     if user.id > 3:
         context = {
         "ls" : Tenant.objects.filter(user = response.user),
         "locations" : Property.objects.filter(tenant = ls),
         "user" : user
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
                else:                       # only management can remove pets from status.
                    if user.id < 4:
                        each.pets =  False

                each.save()




     return render(response, "main/tenants.html", context)

def newTenants(response):
    U = response.user
    if response.method == "POST":
           #print("\nnew property POST\n")
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
               new = Tenant(user =U, firstname = firstN, lastname = lastN, jointtenantname = jointN, pets = pt, paidrent = pr, leaseexpdate = exp, phonenumber = PN, email = EM, address = ad  ) 
               
               # save that input to object list. 
               new.save()

               return HttpResponseRedirect("/tenants")
         
    form = CreateNewTenants()
    if form.is_valid():
        form.save()
    return render(response, "main/newTenant.html", {"form":form})

def newProperty(response):
    if response.method == "POST":
           #print("\nnew property POST\n")
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
        message = ""
        message += "Ticket Number " + response.POST.get("ticketno")
        message += "\t Property " + response.POST.get("item")
        message += "\n\n Tenant " + response.POST.get("tenant")
        catno=  response.POST.get("category")
        urgno = response.POST.get("urgency")
        message += "\t Category " + str(Category.objects.get(id=catno))
        message += " Urgency " + str(Urgency.objects.get(id=urgno))
        message += "\n\n Situation " + response.POST.get("issue")
        
        print(message)
       
        fromEmail = response.user.email
        message_name = str(Category.objects.get(id=catno)) + "issue Urgency Level " +  str(Urgency.objects.get(id=urgno))
        ## send an email.
        send_mail(
            message_name , # subject
            message , # message
            'sherry', # from email
            ['john.schultz@usm.edu'], # to email
            )

        return HttpResponseRedirect("/tickets")

    else:
       form = CreateNewTickets()
       if form.is_valid():
           form.save() 

    return render(response, "main/newTicket.html", {"form":form})




#To add/commit/push:

# in bash terminal (git) navigate to the file ( master)
# git add .
#git commit -m "some comment here"
#git push origin master
 # pw enter in   
 #this submits and saves files and assets to github and local git machine
 # !!!
