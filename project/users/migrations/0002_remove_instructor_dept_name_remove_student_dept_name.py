# Generated by Django 4.0.3 on 2022-03-10 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='dept_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dept_name',
        ),
    ]
