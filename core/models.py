from django.db import models
from django.utils.translation import gettext_lazy as _

class Curso(models.Model):
    nome = models.CharField(max_length=100,verbose_name=_("nome_curso"))
    codigo = models.CharField(max_length=10,unique=True,verbose_name=_("codigo_curso"))
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(_(""),unique=True)
    curso = models.ForeignKey(Curso, verbose_name=_("curso"), on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField('Disciplina')
class Professor(models.Model):
    nome= models.CharField(max_length=100,verbose_name=_("nome_professor"))
    matricula = models.IntegerField(_(""),unique=True, verbose_name=-("matricula_professor"))
class Disciplina(models.Model):
    nome = models.CharField(max_length=100,verbose_name=_("nome_disciplina"))
    codigo = models.CharField(max_length=10,unique=True,verbose_name=_("codigo_disciplina"))
    curso = models.ForeignKey(Curso,verbose_name=_("Curso_disciplina"),on_delete=models.CASCADE)
    Professores =  models.ManyToManyField('Professor')
    alunos = models.ManyToManyField('Aluno')
