# Generated by Django 4.1 on 2022-09-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalfirst', '0007_post_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.CharField(max_length=50),
        ),
    ]
