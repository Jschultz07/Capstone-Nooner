from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("homes/", views.homes, name = "Homes"),
    path("",views.home, name = "landingpage"), #homepage
    path("profile/<int:pk>",views.profile, name = "Profile"),
    path("tickets/",views.tickets, name = "Tickets"),
    path("tenants/",views.tenants, name = "Tenants"),
    path("new/tickets/",views.newTickets, name = "newTickets"),# these will be forms not html pages. or perhaps ... both. 
    path("new/tenants/",views.newTenants, name = "newTenants"),
    path("new/property/",views.newProperty, name = "newProperty")
    

] 
urlpatterns+= staticfiles_urlpatterns()

