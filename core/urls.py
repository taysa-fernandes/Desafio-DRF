from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlunoviewSet,ProfessorViewSet,DisciplinaViewSet,CursoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'alunos',AlunoviewSet, basename='alunos')
router.register(r'professores',ProfessorViewSet,basename='professores')
router.register(r'disciplinas', DisciplinaViewSet,basename='disciplinas')
router.register(r'cursos',CursoViewSet,basename='cursos')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation using Swagger UI",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + router.urls
