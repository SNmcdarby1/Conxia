
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import random_string_generator
from profiles.models import Employee,Store
from .models import Complain
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
import random
from django.db import models

from profiles.models import Client
from django.contrib.auth.models import User

from django.conf import settings
import stripe

# Create your views here.
def book(request):
    if request.user.is_authenticated:
        order_id = None
        return render(request,'book.html',{'order_id':order_id})
    return redirect('login')

def payhome(request):
    if request.POST.get('submit')=='button2':
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        stylist = request.POST.get('stylist')
        date = request.POST.get('date')
        time = request.POST.get('time')
        context = {
            'order_id':order_id,
            'amount':amount,
            'name':name,
            'email':email,
            'service':service,
            'stylist':stylist,
            'date':date,
            'time':time,
            'next':True,
        }
        return render(request,'login.html',context=context)
    
    if request.POST.get('submit')=='button3' and request.user.is_authenticated:
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        stylist = request.POST.get('stylist')
        date = request.POST.get('date')
        time = request.POST.get('time')
        request.session['amount'] = int(float(amount))
        
        obj = Invoice.objects.create(order_id=order_id,name=name,email=email,service=service,stylist=stylist,date=date,time=time,bill=amount)
        context = {
            'key':stripe_pub,
            'amount':float(amount)*100,
            'desp':service,
        }
        return render(request,'stripe_home.html',context=context)
    
    if request.POST.get('submit')=='button1' and request.user.is_authenticated:
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        stylist = request.POST.get('stylist')
        date = request.POST.get('date')
        time = request.POST.get('time')

        obj = Invoice.objects.create(order_id=order_id,name=name,email=email,service=service,stylist=stylist,date=date,time=time,bill=amount)

        payhome = {
            "business": "example@gmail.com",
            "amount": amount,
            "item_name": service,
            "invoice": order_id,
        }

        form = checkoutForm(initial=paypal_dict)
        context = {
            'form':form
        }

        return render(request,'payment_home.html',context=context)
    
    return redirect('home')

@csrf_exempt
def payreturn(request):
    print("Return krk aaya")
    user = request.user
    email = user.email
    order_id = request.POST.get('order_id')
    invoice = Invoice.objects.filter(order_id=order_id).first()
    invoice.paid = True
    invoice.save()
    args = {'post':request.POST,'get':request.GET}
    return render(request,'payment_return.html',args)


def paycancel(request):
    return redirect('home')



def stripecheckout(request):
    print("Here")
    print(request.POST)
    amount = int(request.session.get('amount'))
    customer = stripe.Customer.create(
        email=request.POST.get('stripeEmail'),
        source=request.POST.get('stripeToken')
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Payment'
    )
    
    return render(request,'stripe_success.html',{'amount':amount})

def stripesuccess(request):
    return render(request,'stripe_success.html')


def book(request):
    employees = Employee.objects.values_list('name',flat=True)
    services_ = Service.objects.values_list('name',flat=True)
    services = []
    for i in services_:
        services.append(i)
    context = {
        'employees':employees,
        'services':services,
    }
    return render(request,'book.html')

def home(request):
    services = Service.objects.all()

    return render(request,'home.html',{'services':services})

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        obj = Complain.objects.create(name=name,email=email,subject=subject,message=message)
        messages.info(request,"Thanks for reaching out.We will get in touch soon!!!")
        return redirect('contact')
    return render(request,'contact.html')


class services(models.Model):
    service = models.CharField(max_length=32, null=False, editable=False)
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

class Complain(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)




