# Generated by Django 2.1.4 on 2018-12-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='app.Course'),
        ),
    ]
