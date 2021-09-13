from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('appointment/book', views.appointment, name='book'),
    path('appointment/contact', views.appointment, name='contact'),
    path('appointment/home', views.appointment, name='home'),
    path('appointment/search', views.appointment, name='search'),
    path('appointment/service', views.appointment, name='service'),
    path('appointment/success', views.appointment, name='success'),
]  