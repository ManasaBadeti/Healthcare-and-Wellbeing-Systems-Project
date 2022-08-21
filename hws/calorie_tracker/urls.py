from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r"^index/$", views.index, name="index"),
    url(r"^delete/<int:id>/$", views.delete_consume, name="delete"),
    url(r"^index/$", views.index_view, name="index_view"),
    url(r"^delete/$", views.delete_view, name="delete_view"),


    ]