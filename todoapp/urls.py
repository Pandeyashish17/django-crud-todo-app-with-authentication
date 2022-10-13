from django.urls import path
from . import views
urlpatterns = [
    path("",views.indexPage,name="home"),
    path("login/",views.loginUser,name="login"),
    path("addtodo/",views.addtodoPage,name="addtodo"),
    path("logout/",views.logoutUser,name="logout"),
    path("signin/",views.signInUser,name="signin"),
]
