# Generated by Django 5.1.3 on 2024-12-06 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_alter_cliente_options_alter_interes_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prenda',
            name='capital',
        ),
    ]
