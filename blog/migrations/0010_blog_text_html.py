# Generated by Django 2.2.1 on 2019-05-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190521_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text_html',
            field=models.TextField(default=' ', verbose_name='文章内容（html）'),
            preserve_default=False,
        ),
    ]
