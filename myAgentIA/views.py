from django.shortcuts import render
from django.http import HttpRequest
import ollama

# Create your views here.

def index(request):
    if request.method=="POST":
        question=request.POST.get("textarea")
        response = ollama.chat(model='gemma2:2b', messages=[
        {
            'role': 'user',
            'content': question,
        },
        ])
        
        return render(request,'myAgentIA/index.html',context={'response':response['message']['content'],'question':question})
    return render(request,'myAgentIA/index.html',context={})

def accueil(request):
    return render(request,'myAgentIA/accueil.html')

