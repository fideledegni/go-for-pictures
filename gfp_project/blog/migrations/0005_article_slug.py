# Generated by Django 2.0.3 on 2018-03-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180309_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='an-article-without-slug', max_length=100),
            preserve_default=False,
        ),
    ]
