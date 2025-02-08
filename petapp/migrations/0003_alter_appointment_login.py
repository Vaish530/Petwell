# Generated by Django 5.1.2 on 2024-11-01 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_appointment_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='petapp.login'),
        ),
    ]
