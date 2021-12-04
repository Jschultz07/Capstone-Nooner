from django.db import models
from django.contrib.auth.models import User

class Urgency(models.Model):
    name = models.CharField(max_length=3)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'main_urgency'
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Propertymanagement(models.Model):
    name = models.CharField(max_length=200)

    class Meta: 
        db_table = 'main_propertymanagement'
    def __str__(self):
        return self.name
class Tenant(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    jointtenantname = models.CharField(db_column='jointTenantName', max_length=100, blank = True)  # Field name made lowercase.
    pets = models.BooleanField( blank = True)
    paidrent = models.BooleanField(db_column='paidRent', blank = True)  # Field name made lowercase.
    leaseexpdate = models.CharField(db_column='leaseExpDate', max_length=100)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=14)  # Field name made lowercase.
    email = models.CharField(max_length=40)
    lease = models.CharField(max_length=12000, blank = True)
    address = models.CharField(max_length=100, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    def __str__(self):
        return (self.firstname+" "+self.lastname)

    class Meta:
        
        db_table = 'main_tenant'
class Item(models.Model):
    address = models.CharField(max_length=300)
    rented = models.BooleanField()
    rentprice = models.CharField(db_column='rentPrice', max_length=10)  # Field name made lowercase.
    bedrooms = models.CharField(max_length=5)
    bathrooms = models.CharField(max_length=5)
    propertymanagement = models.ForeignKey(Propertymanagement, on_delete = models.CASCADE, db_column='PropertyManagement_id')  # Field name made lowercase.
    tenant = models.ForeignKey(Tenant, on_delete = models.CASCADE, db_column='Tenant_id')  # Field name made lowercase.
    def __str__(self):
        return self.address
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
class Ticket(models.Model):
    ticketno = models.IntegerField( default = '911', blank = True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=17)  # Field name made lowercase.
    issue = models.CharField(max_length=500)
    complete = models.BooleanField(db_column='Complete', blank = True)  # Field name made lowercase.
    category = models.ForeignKey(Category, on_delete = models.CASCADE, db_column='Category_id')  # Field name made lowercase.
    item = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='Item_id')  # Field name made lowercase.
    tenant = models.ForeignKey(Tenant, on_delete = models.CASCADE, db_column='Tenant_id')  # Field name made lowercase.
    urgency = models.ForeignKey(Urgency, on_delete = models.CASCADE, db_column='Urgency_id' )  # Field name made lowercase.
    notes = models.CharField(max_length=200, blank = True)
    def __str__(self):
        return str(self.ticketno)
    class Meta:
        db_table = 'main_ticket'
class Troubleticket(models.Model):
    issue = models.CharField(max_length=500)
    datereceived = models.CharField(db_column='dateReceived', max_length=25, blank = True)  # Field name made lowercase.
    datecompleted = models.CharField(db_column='dateCompleted', max_length=25)  # Field name made lowercase.
    tenant = models.ForeignKey(Tenant, on_delete = models.CASCADE)

    class Meta:
        
        db_table = 'main_troubleticket'
    def __str__(self):
        return self.id
