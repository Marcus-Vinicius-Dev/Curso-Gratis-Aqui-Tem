# Generated by Django 4.2.6 on 2023-10-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_usuario_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='institution',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
