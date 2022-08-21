from django.conf.urls import url
from .views import (

    register_view,
    user_details,
    bmi_view,
    caltrack,
    dashboard,
    caldetails,
    addtomylist,
    logout,
    weighttrack

)

urlpatterns = [

    url(r"^register/$", register_view, name="register"),
    url(r"^register/dashboard/$", user_details, name="user_details"),
    url(r"^register/$", bmi_view, name="bmi_view"),
    url(r"^homepage/$", logout, name="logout"),
    url(r"^weight/$", weighttrack, name="weighttrack"),

    url(r"^dashboard/$", dashboard, name="dashboard"),

]