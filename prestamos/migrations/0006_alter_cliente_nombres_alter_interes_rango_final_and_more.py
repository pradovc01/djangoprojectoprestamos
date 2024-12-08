# Generated by Django 5.1.3 on 2024-12-08 07:10

import prestamos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0005_remove_prenda_codigo_prestamo_numero_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(max_length=30, validators=[prestamos.validators.validar_string]),
        ),
        migrations.AlterField(
            model_name='interes',
            name='rango_final',
            field=models.IntegerField(null=True, validators=[prestamos.validators.validar_positivos]),
        ),
        migrations.AlterField(
            model_name='interes',
            name='rango_inicial',
            field=models.IntegerField(null=True, validators=[prestamos.validators.validar_positivos]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='numero_pago',
            field=models.IntegerField(null=True, validators=[prestamos.validators.validar_positivos]),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='capital',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[prestamos.validators.validar_positivos]),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='numero_cuotas',
            field=models.IntegerField(null=True, validators=[prestamos.validators.validar_positivos]),
        ),
    ]
