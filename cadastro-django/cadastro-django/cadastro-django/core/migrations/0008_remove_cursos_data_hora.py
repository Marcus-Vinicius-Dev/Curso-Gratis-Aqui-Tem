# Generated by Django 4.2 on 2023-09-08 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cursos_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='data_hora',
        ),
    ]