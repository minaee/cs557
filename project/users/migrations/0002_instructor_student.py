# Generated by Django 4.0.3 on 2022-03-07 08:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('salary', models.FloatField(validators=[django.core.validators.MaxLengthValidator(8, message='No more than 8 digits!'), django.core.validators.MinValueValidator(29000.0, 'Salary should be more than $29000!')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tot_cred', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Credits should be positive values.')])),
            ],
        ),
    ]
