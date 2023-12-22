from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("delete", views.delete, name="delete"),
    path("model", views.model, name="model"),
    path("delete_new", views.delete_new, name="delete_new"),
]