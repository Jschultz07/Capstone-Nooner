from django.contrib import admin
from .models import Urgency, Propertymanagement, Tenant, Item, Ticket, Troubleticket
# Register your models here.
admin.site.register(Propertymanagement)
admin.site.register(Item)
admin.site.register(Tenant)
admin.site.register(Urgency)
admin.site.register(Ticket)
admin.site.register(Troubleticket)