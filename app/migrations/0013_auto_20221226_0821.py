# Generated by Django 3.2.16 on 2022-12-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20221226_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='facebook',
            field=models.CharField(blank=True, default='/', max_length=100, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='info',
            name='facebookAct',
            field=models.BooleanField(default=False, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='info',
            name='instagram',
            field=models.CharField(blank=True, default='/', max_length=100, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='info',
            name='instagramAct',
            field=models.BooleanField(default=False, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='info',
            name='linkedin',
            field=models.CharField(blank=True, default='/', max_length=100, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='info',
            name='linkedinAct',
            field=models.BooleanField(default=False, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='info',
            name='twitter',
            field=models.CharField(blank=True, default='/', max_length=100, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='info',
            name='twitterAct',
            field=models.BooleanField(default=False, verbose_name='Twitter'),
        ),
    ]
