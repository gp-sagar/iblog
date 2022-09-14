# Generated by Django 4.1 on 2022-09-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalfirst', '0002_rename_contactus_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
