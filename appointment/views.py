from django.shortcuts import render,redirect
from .models import Appointment,Service
from .utils import random_string_generator
from .models import Complain
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import random
import requests
from django.urls import reverse

from django import forms
from .models import ConxiaAppointment
from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from products.models import Nail

from profiles.models import UserProfile
# Create your views here.

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
    return render(request,'book.html',context=context)

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





def service(request):

    print(request.POST)
    order_id = random_string_generator()
    email = request.POST.get('email')
    service = request.POST.get('service')
    date = request.POST.get('date')
    time = request.POST.get('time')
    stylist = request.POST.get('employee')
    if stylist == 'Random Stylist':
        stylists = Employee.objects.values_list('name', flat=True)
        print(stylists)
        stylist = random.choice(stylists)
    name  = request.POST.get('name')
    obj = Service.objects.filter(name=service).first()
    try:
        amount = obj.price
    except:
        amount = "N/A"
    context = {
        'pedicure':pedicure,
        'manicure':manicure,
        'fullset':fullset,
        'shellac':shellac,
        'acrylic':acrylic,
        'gell':gell,
        'full manicure':full_manicure,
    }
    return render(request,'success.html',context=context)

    return render(request,'service.html')

def appointment(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')

        obj = Appointment.objects.create(name=name,email=email,service=service,contact=contact,date=date,time=time,note=note)

        return redirect('home')
    return redirect('home')


def get_success_url(self):
    return reverse('conxia:conxiaurl', kwargs={'username': self.kwargs['username']})


    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        message = form.cleaned_data.get("message")
        ChatMessage.objects.create(user=user, thread=thread, message=message)
        return super().form_valid(form)
 
def success(request):
        order_id = random_string_generator()
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        stylist = request.POST.get('employee')

        if stylist == 'Random Stylist':
            stylists = Employee.objects.values_list('name', flat=True)
            print(stylists)
            stylist = random.choice(stylists)

            name  = request.POST.get('name')
            obj = Service.objects.filter(name=service).first()
        try:
            amount = obj.price
        except:
            amount = "N/A"
        context = {
        'email':email,
        'name':name,
        'service':service,
        'stylist':stylist,
        'date':date,
        'time':time,
        'order_id':order_id,
        'contact':contact,
        'amount':amount,
    }
        return render(request,'success.html',context=context)

def search(request):
    store = None
    stores = Store.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        for s in stores:
            if name==s.get_name():
                store = s   
                break
            
    
    store_list = []
    for i in stores:
        store_list.append(i.get_name())

    context = {
        'stores':store_list,
        'store':store,
    }
    return render(request,'search.html',context=context)
