# Generated by Django 4.2.6 on 2023-11-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cursos_instituicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, default='2019-03-28T15:14:19.000Z'),
            preserve_default=False,
        ),
    ]
