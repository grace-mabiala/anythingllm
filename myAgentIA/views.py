from django.shortcuts import render
from django.http import HttpRequest
from django.core.files.storage import FileSystemStorage
import ollama

# Create your views here.

def index(request):
    if request.method=="POST":
        if request.FILES["monFichier"] is not None:
            myfile = request.FILES['monFichier']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
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

