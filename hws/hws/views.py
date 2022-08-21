from django.http import HttpResponse
from django.shortcuts import render


def contactus(request):
    return render(request, 'contactus.html')


def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')

def aboutus(request):
    #return HttpResponse('homepage')
    return render(request,'aboutus.html')
