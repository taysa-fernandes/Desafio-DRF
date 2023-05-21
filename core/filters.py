import django_filters
from .models import Aluno,Curso,Professor,Disciplina

class AlunoModelFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    curso = django_filters.ModelChoiceFilter(queryset=Curso.objects.all(), field_name='curso__nome')
    
    class Meta:
        model = Aluno
        fields = ['nome','matricula','curso']
class ProfessorodelFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    disciplinas = django_filters.Filter(field_name='disciplina')
    
    class Meta:
        model =Professor
        fields = ['nome','disciplina']
        
class DisciplinaModelFilter(django_filters.FilterSet):
    curso = django_filters.NumberFilter(field_name='curso')
    
    class Meta:
        model = Disciplina
        fields = ['curso']
class CursoModelFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Curso
        fields = ['nome'] 