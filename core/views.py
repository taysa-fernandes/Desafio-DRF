from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters import rest_framework as rf
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated



from .models import Aluno,Professor,Curso,Disciplina
from .serializers import AlunoSerializer,ProfessorSerializer,CursoSerializer,DisciplinaSerializer
from .filters import AlunoModelFilter,ProfessorodelFilter,DisciplinaModelFilter,CursoModelFilter

class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filterset_class = AlunoModelFilter
    filter_backends = [filters.SearchFilter,rf.DjangoFilterBackend]
    search_fields = ['nome','matricula']
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        method = 'post',
        request_body = None,
        operation_description = "Método de criar aluno",
        operation_summary="Cria um novo aluno",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['POST'])
    def create(self, request):
        '''Criando um Aluno'''
        return  super().create(request)
    @swagger_auto_schema(
        method = 'put',
        request_body = None,
        operation_description = "Método de atualizar os dados de um aluno",
        operation_summary="Atualiza os dados de um aluno",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PUT'])
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um aluno'''
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'delete',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Aluno", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de deletar os dados de um aluno",
        operation_summary="Deleta os dados de um aluno",
        responses = {200: openapi.Response('Sucess')}
    )
    @api_view(['DELETE'])
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um aluno'''
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'get',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Aluno", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de listar os dados de um aluno específico",
        operation_summary="Lista os dados de um aluno específico",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['GET'])
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um aluno específico'''
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID do Aluno", type=openapi.TYPE_INTEGER),
        openapi.Parameter('nome', openapi.IN_QUERY, description="Nome do Aluno", type=openapi.TYPE_STRING),
        openapi.Parameter('matricula', openapi.IN_QUERY, description="Matrícula do Aluno", type=openapi.TYPE_STRING),
        openapi.Parameter('curso', openapi.IN_QUERY, description="Curso do Aluno", type=openapi.TYPE_STRING),
    ],
        operation_description = "Método de listar os dados dos alunos cadastrados",
        operation_summary="Lista os dados dos alunos",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    def list(self,request, *args, **kwargs):
       '''Listando os alunos cadastrados'''
       return super().list(request,*args,**kwargs)
       
    @swagger_auto_schema(
        method = 'patch',
        request_body = AlunoSerializer,
        operation_description = "Método de atualizar os dados de um aluno inserindo todos os dados",
        operation_summary="Atualiza os dados de um aluno inserindo todos os dados",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PATCH'])
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um aluno'''
        return super().partial_update(request, *args, **kwargs)
    
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filterset_class = ProfessorodelFilter
    filter_backends = [rf.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        method = 'post',
        request_body = None,
        operation_description = "Método de criar professores",
        operation_summary="Cria um novo professor",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['POST'])
    def create(self, request):
        '''Criando um Professor'''
        return super().create(request)
    @swagger_auto_schema(
        method = 'put',
        request_body = None,
        properties={
            'Nome': openapi.Schema(type=openapi.TYPE_STRING),
            'matricula': openapi.Schema(type=openapi.TYPE_INTEGER),
            'disciplinas': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        operation_description = "Método de atualizar os dados de um professor",
        operation_summary="Atualiza os dados de um professor",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PUT'])
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um professor'''
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'delete',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Professor", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de deletar os dados de um professor",
        operation_summary="Deleta os dados de um professor",
        responses = {200: openapi.Response('Sucess')}
    )
    @api_view(['DELETE'])
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um professor'''
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'get',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Professor", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de listar os dados de um Professor específico",
        operation_summary="Lista os dados de um professor específico",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['GET'])
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um professor específico'''
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID do Professor", type=openapi.TYPE_INTEGER),
        openapi.Parameter('nome', openapi.IN_QUERY, description="Nome do Professor", type=openapi.TYPE_STRING),
        openapi.Parameter('matricula', openapi.IN_QUERY, description="Matrícula do Professor", type=openapi.TYPE_STRING),
        openapi.Parameter('disciplinas', openapi.IN_QUERY, description="IDs das Disciplinas dadas pelo Professor", type=openapi.TYPE_INTEGER),
    ],
        operation_description = "Método de listar os dados dos professores cadastrados",
        operation_summary="Lista os dados dos professores",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    def list(self, request, *args, **kwargs):
        '''Listando os professores cadastrados'''
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'patch',
        request_body = ProfessorSerializer,
        operation_description = "Método de atualizar os dados de um professor inserindo todos os dados",
        operation_summary="Atualiza os dados de um professor inserindo todos os dados",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PATCH'])
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um professor'''
        return super().partial_update(request, *args, **kwargs)
    
    
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class =  DisciplinaSerializer
    filterset_class = DisciplinaModelFilter
    filter_backends = [rf.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        method = 'post',
        request_body = None,
        operation_description = "Método de criar disciplina",
        operation_summary="Cria uma nova disciplina",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['POST'])
    def create(self, request):
        '''Criando uma Disciplina'''
        return super().create(request)
    @swagger_auto_schema(
        method = 'put',
        request_body = None,
        operation_description = "Método de atualizar os dados de uma disciplina",
        operation_summary="Atualiza os dados de uma disciplina",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PUT'])
    def update(self, request, *args, **kwargs):
        '''Atualizando Disciplina'''
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'delete',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID da Disciplina", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de deletar os dados de uma disciplina",
        operation_summary="Deleta os dados de uma disciplina",
        responses = {200: openapi.Response('Sucess')}
    )
    @api_view(['DELETE'])
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de uma disciplina'''
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'get',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID da Disciplina", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de listar os dados de uma disciplina específica",
        operation_summary="Lista os dados de uma disciplina específica",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['GET'])
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de uma disciplina específica'''
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID da Disciplina", type=openapi.TYPE_INTEGER),
        openapi.Parameter('nome', openapi.IN_QUERY, description="Nome da Disciplina", type=openapi.TYPE_STRING),
        openapi.Parameter('codigo', openapi.IN_QUERY, description="Código da Disciplina", type=openapi.TYPE_STRING),
        openapi.Parameter('curso', openapi.IN_QUERY, description="Curso da Disciplina", type=openapi.TYPE_INTEGER),
        openapi.Parameter('alunos', openapi.IN_QUERY, description="IDs dos Alunos cadastrados na Disciplina", type=openapi.TYPE_INTEGER),
        openapi.Parameter('professores', openapi.IN_QUERY, description="IDs dos Professores da Disciplina", type=openapi.TYPE_INTEGER),
    ],
        operation_description = "Método de listar os dados das disciplinas cadastradas",
        operation_summary="Lista os dados das disciplinas",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    def list(self, request, *args, **kwargs):
        '''Listando as disciplinas cadastrados'''
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'patch',
        request_body = DisciplinaSerializer,
        operation_description = "Método de atualizar os dados de uma disciplina inserindo todos os dados",
        operation_summary="Atualiza os dados de uma disciplina inserindo todos os dados",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PATCH'])
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de uma disciplina'''
        return super().partial_update(request, *args, **kwargs)
    

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filterset_class = CursoModelFilter
    filter_backends = [rf.DjangoFilterBackend]
    search_fields = ['nome']
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        method = 'post',
        request_body = None,
        operation_description = "Método de criar Curso",
        operation_summary="Cria um novo curso",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['POST'])
    def create(self, request):
        '''Criando um Curso'''
        return super().create(request)
    @swagger_auto_schema(
        method = 'put',
        request_body = None,
        operation_description = "Método de atualizar os dados de um curso",
        operation_summary="Atualiza os dados de um curso",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PUT'])
    def update(self, request, *args, **kwargs):
        '''Atualizando os dados de um curso'''
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'delete',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Curso", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de deletar os dados de um curso",
        operation_summary="Deleta os dados de um curso",
        responses = {200: openapi.Response('Sucess')}
    )
    @api_view(['DELETE'])
    def destroy(self, request, *args, **kwargs):
        '''Excluindo os dados de um curso'''
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'get',
        manual_parameters=[openapi.Parameter('id', openapi.IN_PATH, description="ID do Curso", type=openapi.TYPE_INTEGER)],
        operation_description = "Método de listar os dados de um curso específico",
        operation_summary="Lista os dados de um curso específico",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['GET'])
    def retrieve(self, request, *args, **kwargs):
        '''Listando dados de um curso específico'''
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID do Curso", type=openapi.TYPE_INTEGER),
        openapi.Parameter('nome', openapi.IN_QUERY, description="Nome do Curso", type=openapi.TYPE_STRING),
        openapi.Parameter('codigo', openapi.IN_QUERY, description="Código do Curso", type=openapi.TYPE_STRING),
    ],
        operation_description = "Método de listar os dados dos cursos cadastrados",
        operation_summary="Lista os dados dos cursos",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    def list(self, request, *args, **kwargs):
        '''Listando os cursos cadastrados'''
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        method = 'patch',
        request_body = CursoSerializer,
        operation_description = "Método de atualizar os dados de um curso inserindo todos os dados",
        operation_summary="Atualiza os dados de um curso inserindo todos os dados",
        responses = {200: openapi.Response('Sucess'),400: openapi.Response('Bad Request'),401: openapi.Response('Unauthorized'),500: openapi.Response('Server error')}
    )
    @api_view(['PATCH'])
    def partial_update(self, request, *args, **kwargs):
        '''Atualizando parcialmente os dados de um curso'''
        return super().partial_update(request, *args, **kwargs)
    