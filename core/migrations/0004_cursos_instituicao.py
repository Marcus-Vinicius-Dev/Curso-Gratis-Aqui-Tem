# Generated by Django 4.2.6 on 2023-10-27 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_instituicao_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='instituicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.instituicao'),
            preserve_default=False,
        ),
    ]
