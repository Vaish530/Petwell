# Generated by Django 5.1.2 on 2024-11-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_remove_appointment_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='location',
            field=models.CharField(default='india', max_length=50),
        ),
    ]
