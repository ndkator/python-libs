# Generated by Django 2.0.2 on 2018-03-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basetest', '0011_auto_20180301_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='CommentsText',
            field=models.TextField(verbose_name='Комментарий'),
        ),
    ]
