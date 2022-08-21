from django.conf.urls import url
from .views import (
    login_view,
    bmi_view


)

urlpatterns = [
    url(r'^login/$', login_view, name="login"),
    url(r'^dashboard$', bmi_view, name="bmi_view"),

]