from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlunoviewSet

router = DefaultRouter()
router.register(r'alunos',AlunoviewSet, basename='alunos')

urlpatterns = [
     
] + router.urls
