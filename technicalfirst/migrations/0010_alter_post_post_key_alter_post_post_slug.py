# Generated by Django 4.1 on 2022-09-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalfirst', '0009_remove_post_id_post_post_key_post_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_key',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(unique=True),
        ),
    ]
