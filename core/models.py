from django.db import models
from django.utils.translation import gettext_lazy as _

class Curso(models.Model):
    nome = models.CharField(max_length=100,verbose_name=("nome_curso"))
    codigo = models.CharField(max_length=10,unique=True,verbose_name=("codigo_curso"))
    def __str__(self):
        return self.nome
   
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(unique=True)
    curso = models.ForeignKey(Curso, verbose_name=("curso"), on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
class Professor(models.Model):
    nome= models.CharField(max_length=100,verbose_name=("nome_professor"))
    matricula = models.IntegerField(unique=True)
    def __str__(self):
        return self.nome
class Disciplina(models.Model):
    nome = models.CharField(max_length=100,verbose_name=("nome_disciplina"))
    codigo = models.CharField(max_length=10,unique=True,verbose_name=("codigo_disciplina"))
    curso = models.ForeignKey(Curso,verbose_name=("curso_disciplina"),on_delete=models.CASCADE)
    Professores =  models.ManyToManyField('Professor')
    alunos = models.ManyToManyField('Aluno')
    def __str__(self):
        return self.nome