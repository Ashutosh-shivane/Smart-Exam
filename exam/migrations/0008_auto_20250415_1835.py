# Generated by Django 3.0.5 on 2025-04-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_remove_course_examsubmitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
