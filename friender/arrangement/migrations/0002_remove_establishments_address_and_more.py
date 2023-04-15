# Generated by Django 4.1.7 on 2023-04-11 17:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishments',
            name='address',
        ),
        migrations.RemoveField(
            model_name='establishments',
            name='phone',
        ),
        migrations.AlterField(
            model_name='establishments',
            name='category',
            field=models.CharField(choices=[('r', 'restaurant'), ('c', 'cafe'), ('k', 'bar')], max_length=1),
        ),
        migrations.AlterField(
            model_name='establishments',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrangement.users')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=datetime.datetime)),
                ('passport_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='arrangement.users')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('s', 'sport'), ('t', 'traveling')], max_length=2)),
                ('user', models.ManyToManyField(to='arrangement.users')),
            ],
        ),
        migrations.CreateModel(
            name='EstablishmentsRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrangement.establishments')),
            ],
        ),
        migrations.CreateModel(
            name='Arrangements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrangement.establishments')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrangement.users')),
            ],
        ),
    ]