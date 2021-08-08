# Generated by Django 3.2.6 on 2021-08-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0002_department_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='featured',
        ),
        migrations.AddField(
            model_name='doctor',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]