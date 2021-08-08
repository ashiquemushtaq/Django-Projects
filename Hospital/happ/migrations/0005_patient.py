# Generated by Django 3.2.6 on 2021-08-08 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0004_doctor_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happ.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happ.doctor')),
            ],
        ),
    ]
