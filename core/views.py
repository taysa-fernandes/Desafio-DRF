from django.shortcuts import render
from rest_framework import viewsets



from .models import Aluno,Professor,Curso,Disciplina
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,DisciplinaSerializer
class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
