# Generated by Django 3.2.16 on 2023-01-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_fruit_activ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='activ',
            field=models.BooleanField(default=True, verbose_name='Mostrar'),
        ),
    ]
