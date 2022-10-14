from django.urls import path
from . import views
import random

urlpatterns = [
    path("",views.indexPage,name="home"),
    path("login/",views.loginUser,name="login"),
    path("addtodo/",views.addtodoPage,name="addtodo"),
    path("logout/",views.logoutUser,name="logout"),
    path("signin/",views.signInUser,name="signin"),
    path("delete/sjbcsxx   122443 dbnxcx x234242 cviuv esjcerfh ucbdcnj d8hi45928cvsdscsdw24334432424v 31y21 cv  928ej vddffdxccxbvdc wddxfgdxfgfdsdw9i  k3rwedc/<str:pk>",views.deleteTodo,name="delete"),
    path("update/<str:pk>",views.updateTodo,name="update"),
]
