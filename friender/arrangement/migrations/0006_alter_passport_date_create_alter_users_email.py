# Generated by Django 4.1.7 on 2023-04-30 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0005_establishments_address_establishments_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 30, 12, 51, 18, 453262)),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
