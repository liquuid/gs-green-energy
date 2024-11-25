# Generated by Django 5.1.3 on 2024-11-21 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_habitat_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitat',
            name='consumo_kwh',
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('consumo_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.habitat')),
            ],
        ),
    ]