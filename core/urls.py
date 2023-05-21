from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlunoviewSet,ProfessorViewSet,DisciplinaViewSet,CursoViewSet

router = DefaultRouter()
router.register(r'alunos',AlunoviewSet, basename='alunos')
router.register(r'professores',ProfessorViewSet,basename='professores')
router.register(r'disciplinas', DisciplinaViewSet,basename='disciplinas')
router.register(r'cursos',CursoViewSet,basename='cursos')

urlpatterns = [
     
] + router.urls
