# Generated by Django 3.1.2 on 2021-09-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('starting', models.DateField()),
                ('deadline', models.DateField()),
                ('progress', models.CharField(max_length=20)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('comments', models.CharField(max_length=150)),
                ('duration', models.CharField(max_length=80)),
                ('user', models.CharField(max_length=80)),
            ],
        ),
    ]