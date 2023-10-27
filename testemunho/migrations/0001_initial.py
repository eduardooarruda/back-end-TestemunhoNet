# Generated by Django 4.2.4 on 2023-08-31 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testemunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('conteudo', models.CharField(max_length=3000)),
                ('dataCriacao', models.DateTimeField(auto_now=True)),
                ('autor', models.CharField(max_length=100)),
                ('comentariosAtivo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'testemunho',
                'verbose_name_plural': 'testemunhos',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('conteudo', models.CharField(max_length=600)),
                ('testemunho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='testemunho.testemunho')),
            ],
            options={
                'verbose_name': 'comentário',
                'verbose_name_plural': 'comentários',
            },
        ),
    ]