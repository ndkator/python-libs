# Generated by Django 2.0.2 on 2018-02-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basetest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='Description',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='ReleaseDate',
            field=models.DateField(),
        ),
    ]
