# Generated by Django 3.1.7 on 2021-03-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maven', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
