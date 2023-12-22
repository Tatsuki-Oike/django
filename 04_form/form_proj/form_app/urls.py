from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"), # formの利用
    path("design", views.design, name="design"), # formのデザイン
    path("display", views.display, name="display"), # formの表示形式
    path("val", views.val, name="val"), # formのバリデーション
    path("type", views.type, name="type"), # formの種類
]