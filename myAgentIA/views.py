from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/MyAI/login/")
def index(request):
    print(request.GET.get("workspace"))
    return render(request,'myAgentIA/index.html',context={})

@login_required(login_url="/MyAI/login/")
def accueil(request):
    return render(request,'myAgentIA/accueil.html')


@login_required(login_url="/MyAI/login/")
def workspace(request):
    return render(request,"myAgentIA/workspace.html",context={})

#Login fonction 

def LoginF(request):
    if request.method=="POST":
        nom=request.POST.get("Nom")
        password=request.POST.get("Password")
        user = auth.authenticate(username=nom, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect("accueil")
        else:
            return render(request,"myAgentIA/loginPage.html")
    return render(request,"myAgentIA/loginPage.html")

#Registration fonction

def RegisterF(request):
    if request.method=="POST":
        nom=request.POST.get("Nom")
        email=request.POST.get("Email")
        password=request.POST.get("Password")
    
        try:
            user = User.objects.create_user(username=nom,
                                    email=email,
                                    password=password)
        except:
            error="Un utilisateur avec le même mot de passe existe déjà"
            return render(request,"myAgentIA/registerPage.html",context={'error':error})
                
        else:
            user.save()
            auth.login(request,user)   
        return redirect('accueil')

    return render(request,"myAgentIA/registerPage.html")


def logout_view(request):
    auth.logout(request)
    return redirect("login")
