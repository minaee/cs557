# Generated by Django 4.0.3 on 2022-03-10 09:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=15)),
                ('room_number', models.CharField(max_length=7)),
                ('capacity', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(4, message='No more than 4 digits.')])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('credits', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Credits should be positive values.')])),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(default='Comp. Sci.', max_length=20)),
                ('building', models.CharField(max_length=15)),
                ('budget', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Salary should be positive!')])),
            ],
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_id', models.CharField(max_length=8)),
                ('semester', models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=6)),
                ('year', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.datetime(1701, 1, 1, 0, 0)), django.core.validators.MaxValueValidator(datetime.datetime(2100, 1, 1, 0, 0))])),
                ('time_slot_id', models.CharField(max_length=4)),
            ],
        ),
    ]
