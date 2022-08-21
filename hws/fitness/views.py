from django.shortcuts import render

# Create your views here.
def fitness_view(request):
    return render(request,"fitness/fitnessworkouts.html")