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
    error_message=True
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
           user = User.objects.create_user(username, email, password)
           user.save()
           loggedInUser = authenticate(username=username, password=password)
           if loggedInUser is not None:
              login(request, loggedInUser)
              return redirect("/")
        except:
           error_message=False
    if request.user.is_anonymous:
        return render(request, 'signin.html',)
    else:
        return redirect("home")
    
    



def addtodoPage(request):
    if request.user.is_anonymous:
            return redirect("login")
  
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




def deleteTodo(request,pk):
    if request.user.is_anonymous:
        return redirect("/login")
    todo=todoModel.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("home")
    context={ "todo":todo }

    return render(request, 'delete.html',context)




def updateTodo(request,pk):
    if request.user.is_anonymous:
        return redirect("/login")
    todoToUpdate=todoModel.objects.get(title=pk)
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todoToUpdate.title=title
        todoToUpdate.description=description
        todoToUpdate.save()
        return redirect("home")
    return render(request,"update.html",{"todoToUpdate":todoToUpdate})
    
   
