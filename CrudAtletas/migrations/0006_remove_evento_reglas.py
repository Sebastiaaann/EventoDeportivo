# Generated by Django 5.0 on 2023-12-15 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrudAtletas', '0005_alter_evento_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='reglas',
        ),
    ]
