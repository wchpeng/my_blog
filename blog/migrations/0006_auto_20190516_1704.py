# Generated by Django 2.2.1 on 2019-05-16 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190516_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='expire_to',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='过期时间'),
        ),
    ]
