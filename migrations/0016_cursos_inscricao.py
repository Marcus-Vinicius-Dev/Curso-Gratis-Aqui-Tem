# Generated by Django 4.2 on 2023-10-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_instituicao_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='inscricao',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
