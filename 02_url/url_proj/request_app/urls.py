from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("class/", views.requestClass.as_view(), name="class")
]