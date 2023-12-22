from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("param/<int:id>", views.param, name="param")
]