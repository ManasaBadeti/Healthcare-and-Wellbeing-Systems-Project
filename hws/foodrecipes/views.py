from django.shortcuts import render

# Create your views here.
def foodrecipes_view(request):
    return render(request,"foodrecipes/foods.html")


def recipe_a_view(request):
    return render(request,"foodrecipes/recipe_a.html")

def recipe_b_view(request):
    return render(request,"foodrecipes/recipe_b.html")

def recipe_c_view(request):
    return render(request,"foodrecipes/recipe_c.html")

def recipe_d_view(request):
    return render(request,"foodrecipes/recipe_d.html")

def recipe_e_view(request):
    return render(request,"foodrecipes/recipe_e.html")

def recipe_f_view(request):
    return render(request,"foodrecipes/recipe_f.html")