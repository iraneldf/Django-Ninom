# Generated by Django 3.2.16 on 2022-12-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20221215_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='destinatario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Destinatario',
                'verbose_name_plural': 'Destinatarios',
            },
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
    ]
