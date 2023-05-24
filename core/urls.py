from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlunoviewSet,ProfessorViewSet,DisciplinaViewSet,CursoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'alunos',AlunoviewSet, basename='alunos')
router.register(r'professores',ProfessorViewSet,basename='professores')
router.register(r'disciplinas', DisciplinaViewSet,basename='disciplinas')
router.register(r'cursos',CursoViewSet,basename='cursos')

schema_view = get_schema_view(
    openapi.Info(
        title="API ESCOLA",
        default_version='1.0.0',
        description="Sistema de controle de uma escola",
        #terms_of_service="https://www.example.com/policies/terms/",
        #contact=openapi.Contact(email="contact@example.com"),
        #license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
