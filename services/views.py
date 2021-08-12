from django.shortcuts import render

# Create your views here.
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

from profiles.models import Client
from django.contrib.auth.models import User

from django.conf import settings
im
def services(request):
    return render(request,'services.html')

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

def success(request):
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

