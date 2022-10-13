from django.shortcuts import render,redirect
from .models import todoModel
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User




def indexPage(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    todos=todoModel.objects.filter(user= request.user)
    return render(request, 'index.html',{"todos":todos})
  



def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        return redirect("home")


def signInUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username, email, password)
        user.save()
        loggedInUser = authenticate(username=username, password=password)
        if loggedInUser is not None:
            login(request, loggedInUser)
            return redirect("/")
        else:
            return render(request, 'login.html')
        return redirect("login")
    if request.user.is_anonymous:
        return render(request, 'signin.html')
    else:
        return redirect("home")
  



def addtodoPage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todoform=todoModel(user=request.user,title=title,description=description)
        todoform.save()
        return redirect('home')
    return render(request,'addtodo.html')




def logoutUser(request):
    logout(request)
    return redirect("/login")