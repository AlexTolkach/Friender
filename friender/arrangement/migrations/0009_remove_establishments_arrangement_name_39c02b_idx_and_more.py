# Generated by Django 4.1.7 on 2023-04-30 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0008_alter_passport_date_create_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='establishments',
            name='arrangement_name_39c02b_idx',
        ),
        migrations.RemoveIndex(
            model_name='establishments',
            name='arrangement_name_2cb422_idx',
        ),
        migrations.RemoveIndex(
            model_name='establishments',
            name='arrangement_categor_6b5a37_idx',
        ),
        migrations.RemoveIndex(
            model_name='establishments',
            name='arrangement_categor_05d44e_idx',
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 30, 20, 52, 7, 450862)),
        ),
    ]
