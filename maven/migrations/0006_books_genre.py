# Generated by Django 3.1.7 on 2021-04-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maven', '0005_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
