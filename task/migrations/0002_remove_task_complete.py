# Generated by Django 3.2.9 on 2022-03-04 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
    ]