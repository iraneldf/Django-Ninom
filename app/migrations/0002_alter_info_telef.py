# Generated by Django 3.2.16 on 2022-12-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='telef',
            field=models.CharField(default='', max_length=100, verbose_name='Telef'),
        ),
    ]
