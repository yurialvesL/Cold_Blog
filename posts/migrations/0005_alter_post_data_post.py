# Generated by Django 4.0.4 on 2022-07-11 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 14, 35, 3, 165172, tzinfo=utc)),
        ),
    ]
