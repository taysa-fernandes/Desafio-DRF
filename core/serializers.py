from rest_framework import serializers
from .models import Aluno,Professor,Disciplina,Curso

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso','id','disciplinas']
        extra_kwargs = {
            'disciplinas': {
                'source': 'disciplina_set'
            }
        }
        
class ProfessorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Professor
        fields = ['nome','matricula','id']

class DisciplinaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Disciplina
        fields = ['nome','codigo','curso','alunos','Professores','id']
        
class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = ['nome','codigo','id']
