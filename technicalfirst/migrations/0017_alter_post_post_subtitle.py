# Generated by Django 4.1 on 2022-09-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalfirst', '0016_post_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_subtitle',
            field=models.TextField(default=''),
        ),
    ]
