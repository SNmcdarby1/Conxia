from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.userprofile.save()



class Store(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
    
    
    def get_name(self):
        return self.name + " , " + self.location

class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)
    taxes = models.CharField(max_length=10,blank=True,null=True)
    leaves = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.name+" "+str(self.user.email)


class Store(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
    
    
    def get_name(self):
        return self.name + " , " + self.location

class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)
    taxes = models.CharField(max_length=10,blank=True,null=True)
    leaves = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.name+" "+str(self.user.email)

