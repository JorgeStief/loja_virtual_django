# Generated by Django 2.2.7 on 2019-11-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_auto_20191110_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='main_image',
            field=models.FileField(default=None, upload_to='media/%Y-%m-%d/', verbose_name='Imagem Principal'),
        ),
    ]
