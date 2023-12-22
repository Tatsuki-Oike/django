from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="crud_home"),
    path("create", views.create, name="create"),
    path("delete", views.delete_all, name="delete_all"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path('logout/', views.custom_logout, name='logout'),
]