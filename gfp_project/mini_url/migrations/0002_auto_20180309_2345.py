# Generated by Django 2.0.3 on 2018-03-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='longURL',
            field=models.URLField(unique=True, verbose_name='URL à réduire'),
        ),
    ]
