# Generated by Django 4.1 on 2022-09-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalfirst', '0008_alter_post_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='post_key',
            field=models.IntegerField(default='8293', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(default='skjdfnkj', unique=True),
        ),
    ]
