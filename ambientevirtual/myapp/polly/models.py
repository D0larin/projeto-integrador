from django.db import models


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    
    

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    professores = models.ManyToManyField(Professor, related_name='alunos')
    nome = models.CharField(max_length=200)
   

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    professor = models.OneToOneField(Professor, related_name='sala', on_delete=models.SET_NULL, null=True)
    numero = models.IntegerField()
