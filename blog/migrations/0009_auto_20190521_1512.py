# Generated by Django 2.2.1 on 2019-05-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_is_md'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_md',
            field=models.BooleanField(verbose_name='markdown'),
        ),
    ]