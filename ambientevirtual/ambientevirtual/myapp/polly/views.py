from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Sala, Professor, Aluno, Show


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
    

@login_required(login_url='/login')
def aluno(request):
    if request.method == "GET":
        return render(request, "aluno.html")
    elif request.method == "POST":
        nome = request.POST["nome"]
        if Aluno.objects.filter(nome = nome).exists():
            return HttpResponse('Este nome já está cadastrado')
        else:
            novo_aluno = Aluno.objects.create(nome=nome)
            return redirect('/')
    else:
        return HttpResponseBadRequest()
            

@login_required(login_url='/login')
def professor(request):
    if  request.method == "GET":
       return render(request, "professor.html")
    elif request.method == "POST":
        nome = request.POST["nome"]
        if Professor.objects.filter(nome=nome).exists():
            return HttpResponse('Este nome já está cadastrado')
        else:
            novo_prof = Professor.objects.create( nome=nome)
            return redirect('/')
    else:
        return HttpResponseBadRequest()


@login_required(login_url='/login')
def sala(request):
    if request.method == "GET":
        return render(request, "sala.html")
    elif request.method == "POST":
        numero = request.POST["numero"]
        if Sala.objects.filter(numero=numero).exists():
            return HttpResponse('Este numero já está cadastrado')
        else:
            novo_numero = Sala.objects.create(numero=numero)
            return redirect('/')
    else:
        return HttpResponseBadRequest()
    

def logout(request):
    if logout(request):
        return redirect("/login")
    else:
        return HttpResponseBadRequest()
    

def manejamento(request):
    return render(request, "manejamento.html")


def organizador(request):
    if request.method == 'GET':
        return render(request, 'organizador.html')
    elif request.method == 'POST':
        n_sala = request.POST['n_sala']
        nome_prof = request.POST['nome_prof']
        nome_aluno = request.POST['nome_aluno']
        
        if not Sala.objects.filter(numero=n_sala).exists():
            return HttpResponse('Este número de sala não está cadastrado')
        else:
            s = Sala.objects.get(numero=n_sala)

        if not Professor.objects.filter(nome=nome_prof).exists():
            return HttpResponse('Este nome de professor não está cadastrado')
        else:
            p = Professor.objects.get(nome=nome_prof)

        if not Aluno.objects.filter(nome=nome_aluno).exists():
            return HttpResponse('Este nome de aluno não está cadastrado')
        else:
            a = Aluno.objects.get(nome=nome_aluno)
            
        Show.objects.create(sala=s, professor=p, aluno=a)
        
        return redirect('/')
    else:
        return HttpResponseBadRequest()