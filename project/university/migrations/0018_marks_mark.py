# Generated by Django 4.0.3 on 2022-04-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0017_marks_take'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='mark',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]