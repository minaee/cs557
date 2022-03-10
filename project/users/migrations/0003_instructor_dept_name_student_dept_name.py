# Generated by Django 4.0.3 on 2022-03-10 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_initial'),
        ('users', '0002_remove_instructor_dept_name_remove_student_dept_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='dept_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='dept_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department'),
        ),
    ]
