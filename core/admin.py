from django.contrib import admin
from .models import Aluno,Professor,Disciplina,Curso

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso','disciplinas')
admin.site.register(Aluno,AlunoAdmin)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome_professor','matricula_professor')
admin.site.register(Professor,ProfessorAdmin)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome_disciplina','codigo_disciplina','curso_disciplina','professores','alunos')
admin.site.register(Disciplina,DisciplinaAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'codigo_curso')