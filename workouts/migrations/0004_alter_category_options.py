# Generated by Django 3.2.8 on 2021-12-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_workout_weeks_of_plan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
