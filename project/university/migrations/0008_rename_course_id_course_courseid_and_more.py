# Generated by Django 4.0.3 on 2022-03-12 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_alter_section_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_id',
            new_name='courseId',
        ),
        migrations.RenameField(
            model_name='prereq',
            old_name='course_id',
            new_name='courseId',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='course_id',
            new_name='courseId',
        ),
        migrations.RenameField(
            model_name='takes',
            old_name='course_id',
            new_name='courseId',
        ),
        migrations.RenameField(
            model_name='teaches',
            old_name='course_id',
            new_name='courseId',
        ),
    ]