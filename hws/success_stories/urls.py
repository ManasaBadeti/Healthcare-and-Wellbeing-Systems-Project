from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^dss/$",views.stories_view, name="stories_view"),

    url(r"^ss/$", views.enterstories_view, name="enterstories"),
    url(r"^ss/dss$", views.enter_stories, name="enter_stories"),





    ]