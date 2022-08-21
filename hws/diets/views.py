from django.shortcuts import render

# Create your views here.
def diets_view(request):
    return render(request,"diets/diets.html")