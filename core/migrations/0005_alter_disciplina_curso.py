# Generated by Django 3.2.19 on 2023-05-21 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_aluno_disciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='curso_disciplina'),
        ),
    ]