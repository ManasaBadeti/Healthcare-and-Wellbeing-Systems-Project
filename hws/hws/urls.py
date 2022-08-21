"""hws URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/', include('register.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^calorie_tracker/', include('calorie_tracker.urls')),
    url(r'^diets/', include('diets.urls')),
    url(r'^fitness/', include('fitness.urls')),
    url(r'^success_stories/', include('success_stories.urls')),
    url(r'^foodrecipes/', include('foodrecipes.urls')),
    url(r'^$',views.homepage,name="homepage"),
    url(r'^contactus/$',views.contactus, name="contactus"),
    url(r'^aboutus/$',views.aboutus, name="aboutus"),


    #path('',views.homepage),
    #path('contactus/',views.contactus)

]
