# Generated by Django 3.1.2 on 2021-09-27 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20210927_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='comments',
        ),
    ]
