from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^diets/$",views.diets_view, name="diets_view" ),
    ]