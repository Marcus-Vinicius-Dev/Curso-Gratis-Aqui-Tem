# Generated by Django 4.2 on 2023-09-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_cursos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='categoria',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
