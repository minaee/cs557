# Generated by Django 4.0.3 on 2022-03-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_instructor_dept_name_student_dept_name'),
        ('university', '0013_takes_student_alter_takes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takes',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]