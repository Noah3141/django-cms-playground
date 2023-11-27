from django.urls import path

from . import views


app_name = "apples" # Namespaces the "name" values below
urlpatterns = [
    path("", views.apple, name="index"),
]