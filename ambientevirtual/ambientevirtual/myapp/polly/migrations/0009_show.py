# Generated by Django 5.0.2 on 2024-03-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polly', '0008_delete_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.IntegerField()),
                ('professor', models.CharField(max_length=200)),
                ('aluno', models.CharField(max_length=200)),
            ],
        ),
    ]
