# Generated by Django 4.2 on 2023-10-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_cursos_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='inscricao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
