# Generated by Django 2.1.4 on 2018-12-27 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_logintype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
