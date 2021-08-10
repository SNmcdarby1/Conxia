from django.urls import path
from . import views

urlpatterns = [
    path('services', views.service, name= 'services') 
    path('book', views.book, name= 'book')
    path('contact', views.contact, name= 'contact')
    path('home', views.home, name= 'home')
    path('search', views.search, name= 'ssearch')
    path('success', views.success, name= 'success')
]