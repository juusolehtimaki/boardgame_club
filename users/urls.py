from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = 'users'

urlpatterns = [
    
    path ('',include('django.contrib.auth.urls')),
    # Registration page.
    path ('register/',views.register, name='register'),
    
    ]