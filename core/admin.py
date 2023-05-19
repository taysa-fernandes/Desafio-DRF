from django.contrib import admin
from .models import Aluno,Professor,Disciplina,Curso

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso')
admin.site.register(Aluno,AlunoAdmin)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula')
admin.site.register(Professor,ProfessorAdmin)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome','codigo','curso')
admin.site.register(Disciplina,DisciplinaAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
admin.site.register(Curso,CursoAdmin)