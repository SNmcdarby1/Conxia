from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    service = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    time = models.CharField(max_length=10,blank=True,null=True)
    note = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name + " " + str(self.email) + " " +str(self.contact)

class ConxiaAppointment(models.Model):
    ConxiaAppointment = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    # order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # original_bag = models.TextField(null=False, blank=False, default='')
    # stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


class Complain(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name + " " + str(self.email)



