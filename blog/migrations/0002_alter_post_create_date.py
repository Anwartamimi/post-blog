# Generated by Django 4.1.7 on 2023-02-19 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 19, 10, 55, 55, 431487, tzinfo=datetime.timezone.utc)),
        ),
    ]
