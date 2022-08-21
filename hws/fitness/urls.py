from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^fitnessworkouts/$",views.fitness_view, name="fitness_view" ),

    ]