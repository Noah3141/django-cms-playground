from django.urls import path

from . import views


app_name = "zolls" # Namespaces the "name" values below
urlpatterns = [
    path("", views.zoll, name="index"),
]