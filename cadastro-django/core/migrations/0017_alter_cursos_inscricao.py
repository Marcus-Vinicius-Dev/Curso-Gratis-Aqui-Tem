# Generated by Django 4.2 on 2023-10-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_cursos_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='inscricao',
            field=models.DateField(),
        ),
    ]