from django.shortcuts import render
from rest_framework import viewsets

from .models import Aluno,Professor,Curso,Disciplina
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,DisciplinaSerializer
class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class =  DisciplinaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer