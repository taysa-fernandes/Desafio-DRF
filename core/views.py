from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters import rest_framework as rf
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema



from .models import Aluno,Professor,Curso,Disciplina
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,DisciplinaSerializer
from .filters import AlunoModelFilter,ProfessorodelFilter,DisciplinaModelFilter,CursoModelFilter

class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filterset_class = AlunoModelFilter
    filter_backends = [filters.SearchFilter,rf.DjangoFilterBackend]
    search_fields = ['nome','matricula']
    @extend_schema(
        request=AlunoSerializer,
        responses={
            200: 'sucess'},
        description='Método de criar aluno',
        summary="Cria um novo aluno", 
    )
    @swagger_auto_schema(
        operation_description = "criar objeto",
        Responses = {200: 'sucess'}
    )
    def create(self, request):
        '''Criando um Aluno'''
        return  Response(data={'message': 'Sucess'}, status=status.HTTP_200_OK)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar os dados de um aluno inserindo todos os campos',
        summary="Atualiza os dados de um aluno", 
    )
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um aluno'''
        return super().update(request, *args, **kwargs)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de deletar os dados de um aluno',
        summary="Deleta os dados de um aluno", 
    )
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um aluno'''
        return super().destroy(request, *args, **kwargs)
    @extend_schema(
        request=AlunoSerializer,
        responses={200: 'sucess'},
        description='Método de listar dados de um aluno específico',
        summary="Lista dados de um aluno", 
    )
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um aluno específico'''
        return super().retrieve(request, *args, **kwargs)
    @extend_schema(
        request=AlunoSerializer,
        responses={200: 'sucesso'},
        description='Método de listar os alunos cadastrados',
        summary="Lista alunos cadastrados", 
    )
    def list(self, request, *args, **kwargs):
        '''Listando os alunos cadastrados'''
        return super().list(request, *args, **kwargs)
    @extend_schema(
        request=AlunoSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar um aluno parcialmente',
        summary="Atualiza parcialmente os dados de um aluno", 
    )
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um aluno'''
        return super().partial_update(request, *args, **kwargs)
    
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filterset_class = ProfessorodelFilter
    filter_backends = [rf.DjangoFilterBackend]
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de criar professor',
        summary="Cria um novo professor", 
    )
    def create(self, request):
        '''Criando um Professor'''
        return super().create(request)
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar os dados de um professor inserindo todos os campos',
        summary="Atualiza os dados de um professor", 
    )
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um professor'''
        return super().update(request, *args, **kwargs)
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de deletar os dados de um professor',
        summary="Deleta os dados de um professor", 
    )
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um professor'''
        return super().destroy(request, *args, **kwargs)
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de listar dados de um professor específico',
        summary="Lista dados de um professor", 
    )
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um professor específico'''
        return super().retrieve(request, *args, **kwargs)
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de listar os professores cadastrados',
        summary="Lista professores cadastrados", 
    )
    def list(self, request, *args, **kwargs):
        '''Listando os professores cadastrados'''
        return super().list(request, *args, **kwargs)
    @extend_schema(
        request=ProfessorSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar um professor parcialmente',
        summary="Atualiza parcialmente os dados de um professor", 
    )
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um professor'''
        return super().partial_update(request, *args, **kwargs)
    
    
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class =  DisciplinaSerializer
    filterset_class = DisciplinaModelFilter
    filter_backends = [rf.DjangoFilterBackend]
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de criar disciplina',
        summary="Cria uma nova disciplina", 
    )
    def create(self, request):
        '''Criando uma Disciplina'''
        return super().create(request)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar uma disciplina inserindo todos os campos',
        summary="Atualiza uma disciplina", 
    )
    def update(self, request, *args, **kwargs):
        '''Atualizando Disciplina'''
        return super().update(request, *args, **kwargs)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de deletar os dados de uma disciplina',
        summary="Deleta os dados de uma disciplina", 
    )
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de uma disciplina'''
        return super().destroy(request, *args, **kwargs)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de listar dados de uma disciplina específica',
        summary="Lista dados de uma disciplina", 
    )
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de uma disciplina específica'''
        return super().retrieve(request, *args, **kwargs)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de listar as disciplinas cadastradas',
        summary="Lista disciplinas cadastradas", 
    )
    def list(self, request, *args, **kwargs):
        '''Listando as disciplinas cadastrados'''
        return super().list(request, *args, **kwargs)
    @extend_schema(
        request=DisciplinaSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar uma disciplina parcialmente',
        summary="Atualiza parcialmente os dados de uma disciplina", 
    )
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de uma disciplina'''
        return super().partial_update(request, *args, **kwargs)
    

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filterset_class = CursoModelFilter
    filter_backends = [rf.DjangoFilterBackend]
    search_fields = ['nome']
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de criar curso',
        summary="Cria um novo curso", 
    )
    def create(self, request):
        '''Criando um Curso'''
        return super().create(request)
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar os dados de um curso inserindo todos os campos',
        summary="Atualiza os dados de um curso", 
    )
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um curso'''
        return super().update(request, *args, **kwargs)
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de deletar os dados de um curso',
        summary="Deleta os dados de um curso", 
    )
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um curso'''
        return super().destroy(request, *args, **kwargs)
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de listar dados de um curso específico',
        summary="Lista dados de um curso", 
    )
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um curso específico'''
        return super().retrieve(request, *args, **kwargs)
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de listar os cursos cadastrados',
        summary="Lista cursos cadastrados", 
    )
    def list(self, request, *args, **kwargs):
        '''Listando os cursos cadastrados'''
        return super().list(request, *args, **kwargs)
    @extend_schema(
        request=CursoSerializer,
        responses={200: 'sucess'},
        description='Método de atualizar um curso parcialmente',
        summary="Atualiza parcialmente os dados de um curso", 
    )
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um curso'''
        return super().partial_update(request, *args, **kwargs)
    