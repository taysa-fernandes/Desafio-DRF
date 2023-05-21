from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters import rest_framework as rf

from .models import Aluno,Professor,Curso,Disciplina
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,DisciplinaSerializer
from .filters import AlunoModelFilter,ProfessorodelFilter,DisciplinaModelFilter,CursoModelFilter
class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filterset_class = AlunoModelFilter
    filter_backends = [filters.SearchFilter,rf.DjangoFilterBackend]
    search_fields = ['nome','matricula']
    
    
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filterset_class = ProfessorodelFilter
    filter_backends = [rf.DjangoFilterBackend]
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class =  DisciplinaSerializer
    filterset_class = DisciplinaModelFilter
    filter_backends = [rf.DjangoFilterBackend]

    

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filterset_class = CursoModelFilter
    filter_backends = [rf.DjangoFilterBackend]
    search_fields = ['nome']
    