"""conxia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointment.views import home,appointment,contact,service,book,success,search
# from profiles.views import LoginUser,RegisterUser,Logout_view,ActivateAccount,dashboard,password
# from payment.views import payhome,paycancel,payreturn,stripesuccess,checkout,stripecheckout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('appointment/', include('appointment.urls')),
    # path('appointment/service/', include('appointment/service.urls')),
    # path('appointment/book/', include('appointment/book.urls')),
    # path('appointment/search/', include('appointment/search.urls')),
    # path('appointment/success/', include('appointment/success.urls')),
    # path('appointment/contact/', include('appointment/contact.urls')),
   
    # path('payment/', include('payment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
