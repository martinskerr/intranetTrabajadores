# Generated by Django 4.2.7 on 2023-11-23 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Empleador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleador', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_seccion', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipodocumento', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tiposolicitud', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_trabajador', models.CharField(max_length=80)),
                ('rut_trabajador', models.CharField(max_length=15, unique=True)),
                ('fechaingreso_trabajador', models.DateField()),
                ('estado_trabajador', models.BooleanField()),
                ('fk_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.area')),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.empresa')),
                ('fk_seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.seccion')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_telefono', models.IntegerField()),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tarea', models.CharField(max_length=55)),
                ('fecha_tarea', models.DateField()),
                ('fk_empleador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.empleador')),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('estado_solicitud', models.CharField(max_length=15)),
                ('fk_tiposolicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.tiposolicitud')),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='SaldoVacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_vacaciones', models.FloatField()),
                ('fechainicio_sueldo', models.DateField()),
                ('fechafin_sueldo', models.DateField()),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_email', models.CharField(max_length=30)),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta_documento', models.FileField(upload_to='')),
                ('fechasolicitud_documento', models.DateField()),
                ('fk_empleador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.empleador')),
                ('fk_tipodocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.tipodocumento')),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_directorio', models.CharField(max_length=55)),
                ('fk_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.area')),
                ('fk_seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(max_length=55)),
                ('fk_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajadorApp.trabajador')),
            ],
        ),
    ]
