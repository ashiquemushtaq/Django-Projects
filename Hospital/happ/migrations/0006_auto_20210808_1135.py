# Generated by Django 3.2.6 on 2021-08-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0005_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.CharField(max_length=50),
        ),
    ]
