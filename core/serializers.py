from rest_framework import serializers
from .models import Aluno,Professor,Disciplina,Curso

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso','disciplinas']
        
class ProfessorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Professor
        fields = ['nome','matricula']

class DisciplinaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Disciplina
        fields = ['nome','codigo','curso','professores','alunos']
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = ['nome','codigo']
