# Generated by Django 3.2.5 on 2021-08-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodkartapp', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=1, upload_to='category_pic'),
            preserve_default=False,
        ),
    ]