from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^foods/$",views.foodrecipes_view, name="foodrecipes_view" ),
    url(r"^recipe_a/$",views.recipe_a_view, name="recipe_a" ),
    url(r"^recipe_b/$", views.recipe_b_view, name="recipe_b"),
    url(r"^recipe_c/$", views.recipe_c_view, name="recipe_c"),
    url(r"^recipe_d/$", views.recipe_d_view, name="recipe_d"),
    url(r"^recipe_e/$", views.recipe_e_view, name="recipe_e"),
    url(r"^recipe_f/$", views.recipe_f_view, name="recipe_f"),

    ]