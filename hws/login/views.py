

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm



def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return render(request,"register/dashboard.html")
	return render(request, "login/form.html", {
		"form" : form,
		"title" : "Login",
	})

def bmi_view(request):
	return render(request,"register/bmi.html")