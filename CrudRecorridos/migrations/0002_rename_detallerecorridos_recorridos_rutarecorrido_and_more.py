# Generated by Django 4.2.5 on 2023-12-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CrudVehiculos', '0003_remove_vehiculos_comentarios_vehiculos_comentario'),
        ('CrudConductores', '0003_alter_conductores_licencia'),
        ('CrudRecorridos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recorridos',
            old_name='detalleRecorridos',
            new_name='rutaRecorrido',
        ),
        migrations.RemoveField(
            model_name='recorridos',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='recorridos',
            name='ruta',
        ),
        migrations.AddField(
            model_name='recorridos',
            name='ganancia',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorridos',
            name='gasto',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorridos',
            name='recorridoID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recorridos',
            name='vehiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CrudVehiculos.vehiculos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recorridos',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CrudConductores.conductores'),
        ),
    ]