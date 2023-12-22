from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user_home"),
    path('login/', views.CustomUserLoginView.as_view(), name='login'),
    path("signup/", views.signup, name="signup"),
]