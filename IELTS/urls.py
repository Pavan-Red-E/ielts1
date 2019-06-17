"""IELTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from app.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/', register),
    url('home/register/login/check/checkscorepage/', checkscorepage),
    url('home/register/login/check/checkscore/', checkscore),
    url('home/contact-us/', contactpage),
    url('home/rules/', rulespage),
    url('home/analytics/', analyticspage),
    url('home/register/', register),
    url('home/register/login/', login),
    url('home/register/login/check/', checklogin),
    url('home/register/saveuser/', saveuser),
]
