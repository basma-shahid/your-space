# Generated by Django 3.2.4 on 2021-07-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_profile_timeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timeslots',
            field=models.ManyToManyField(to='main_app.Timeslot'),
        ),
    ]
