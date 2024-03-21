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
    nome = models.CharField(max_length=200)
   

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(unique=True)

class Show(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)