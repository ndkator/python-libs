# Generated by Django 2.0.2 on 2018-02-28 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basetest', '0004_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, unique=True)),
                ('Birthday', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comments_article',
            new_name='LibraryID',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_text',
        ),
        migrations.AddField(
            model_name='comments',
            name='AddDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='CommentsText',
            field=models.CharField(default='Пустой комментарий', max_length=255),
        ),
        migrations.AddField(
            model_name='comments',
            name='UserID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='basetest.Users'),
        ),
    ]
