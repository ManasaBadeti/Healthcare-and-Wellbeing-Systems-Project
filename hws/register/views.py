from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Details
from .forms import UsersRegisterForm


# Create your views here.
def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return render(request,'register/details.html')
	return render(request, 'register/register.html', {
		"title": "Register",
		"form": form,
	})



def user_details(request):
   name = request.POST['name']
   dob = request.POST['dob']
   weight = request.POST['weight']
   height = request.POST['height']
   ins=Details(name=name, dob=dob,weight=weight,height=height)
   ins.save()

   return render(request, 'register/dashboard.html')


def bmi_view(request):
	return render(request,"register/bmi.html")

def caltrack(request):
	return render(request,"register/caladdtomylist.html")

def addtomylist(request):
	return render(request,"register/caldetails.html")


def dashboard(request):
	return render(request,"register/dashboard.html")


def caldetails(request):
	return render(request,"register/caldetails.html")



def logout(request):
	return render(request,"homepage.html")

def weighttrack(request):
	return render(request,"register/weight.html")


