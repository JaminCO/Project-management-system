# Generated by Django 3.1.2 on 2021-09-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210924_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, default='no description...', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='no description...', null=True),
        ),
    ]
