# Generated by Django 2.0.3 on 2019-11-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_is_addtimeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_addtimeline',
            field=models.BooleanField(default=False, verbose_name='是否添加时间线'),
        ),
    ]
