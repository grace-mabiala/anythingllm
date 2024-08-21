from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/MyAI/login/")
def index(request):
    return render(request,'myAgentIA/index.html',context={})

@login_required(login_url="/MyAI/login/")
def accueil(request):
    return render(request,'myAgentIA/accueil.html')

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

def RegisterF(request):
    if request.method=="POST":
        nom=request.POST.get("Nom")
        email=request.POST.get("Email")
        password=request.POST.get("Password")
        u = User.objects.get(username=password)
        if u is None:
            user = User.objects.create_user(username=nom,
                                email=email,
                                password=password)
            user.save()
        return redirect('accueil')

    return render(request,"myAgentIA/registerPage.html")


def logout_view(request):
    auth.logout(request)
    return redirect("login")
