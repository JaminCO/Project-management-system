# Generated by Django 3.1.2 on 2021-12-18 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20211218_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='task',
            name='progress',
        ),
    ]
