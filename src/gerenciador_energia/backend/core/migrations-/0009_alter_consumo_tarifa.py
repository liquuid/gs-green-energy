# Generated by Django 5.1.3 on 2024-11-21 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_consumo_habitat_alter_consumo_tarifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='tarifa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tarifaenergia'),
        ),
    ]
