# Generated by Django 5.0.2 on 2024-03-20 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polly', '0005_show_delete_manejamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='professores',
            field=models.ManyToManyField(related_name='alunos', to='polly.professor'),
        ),
        migrations.AddField(
            model_name='sala',
            name='professor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sala', to='polly.professor'),
        ),
        migrations.DeleteModel(
            name='Show',
        ),
    ]
