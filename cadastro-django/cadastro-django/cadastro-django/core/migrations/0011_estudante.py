# Generated by Django 4.0.6 on 2023-09-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_instituicao_cnpj_instituicao_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=3)),
            ],
        ),
    ]