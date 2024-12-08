# Generated by Django 5.1.3 on 2024-12-06 21:18

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('ci', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now_add=True)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasa', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name': 'Interes',
                'verbose_name_plural': 'Interes',
                'db_table': 'interes',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('categoria', models.CharField(choices=[('JO', 'Joya'), ('MO', 'Movilidad'), ('MOT', 'Motocicleta')], default='JO', max_length=3)),
                ('capital', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Prenda',
                'verbose_name_plural': 'Prendas',
                'db_table': 'prenda',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('capital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activo', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.cliente')),
                ('interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.interes')),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prenda')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
                'db_table': 'prestamo',
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo_pago', models.CharField(choices=[('IN', 'Interes'), ('PA', 'Pago')], default='IN', max_length=2)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
                'db_table': 'pago',
                'ordering': [builtins.id],
            },
        ),
    ]
