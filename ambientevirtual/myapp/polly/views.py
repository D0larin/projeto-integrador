from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Sala, Professor, Aluno


@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {
                'login_incorreto': True 
            })
    return render(request, 'login.html', {
        'login_incorreto':False
    })
        
       
def Cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["password"]
        if User.objects.filter(username=email).exists():
            return HttpResponse('Este email já foi cadastrado')
        else:
            user = User.objects.create_user(email, email, senha)
        return redirect('/login')
    else:
        return HttpResponseBadRequest()
    

def aluno(request):
    if request.method == "GET":
        return render(request, "aluno.html")
    elif request.method == "POST":
        nome = request.POST["nome"]
        prof = request.POST["prof"] 


def professor(request):
    if  request.method == "GET":
       return render(request, "professor.html")
    elif request.method == "POST":
        nome = request.POST["nome"]



def sala(request):
    if request.method == "GET":
        return render(request, "sala.html")
    elif request.method == "POST":
        numero = request.POST["numero"]