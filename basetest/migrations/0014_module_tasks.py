# Generated by Django 2.0.2 on 2018-03-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basetest', '0013_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='tasks',
            field=models.ManyToManyField(to='basetest.Task'),
        ),
    ]