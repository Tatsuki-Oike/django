from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.data, name="data"),
    path("syntax", views.syntax, name="syntax"),
    path("change", views.change, name="change"),
    path("design", views.design, name="design"),
    path("layout", views.layout, name="layout")
]