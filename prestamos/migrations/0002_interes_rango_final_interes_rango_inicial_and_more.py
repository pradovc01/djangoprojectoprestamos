# Generated by Django 5.1.3 on 2024-12-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interes',
            name='rango_final',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='interes',
            name='rango_inicial',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='numero_pago',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='numero_cuotas',
            field=models.IntegerField(null=True),
        ),
    ]
