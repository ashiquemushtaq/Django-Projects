# Generated by Django 3.2.5 on 2021-07-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodkartapp', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
