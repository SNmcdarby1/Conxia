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


SEVICE_TYPE = service

class Service(models.Model):
    user = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    type = models.CharField(max_length=10,choices=SERVICE_TYPE)
    amount = models.DecimalField(default=0.00,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.user.name