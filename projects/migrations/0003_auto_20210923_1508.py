# Generated by Django 3.1.2 on 2021-09-23 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210923_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ('-created',)},
        ),
    ]
