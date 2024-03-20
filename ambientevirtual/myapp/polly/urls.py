from django.urls import path
from polly  import views

urlpatterns = [
    path("", views.index),
    path("login", views.login_view),
    path("cadastro", views.Cadastro),
    path("aluno", views.aluno),
    path("professor", views.professor),
    path("sala", views.sala),
]
