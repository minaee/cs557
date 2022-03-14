# Generated by Django 4.0.3 on 2022-03-14 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_instructor_dept_name_student_dept_name'),
        ('university', '0012_alter_section_courseid'),
    ]

    operations = [
        migrations.AddField(
            model_name='takes',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]