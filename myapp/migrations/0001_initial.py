# Generated by Django 5.0.6 on 2024-06-03 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=10000)),
                ('date_post', models.DateField(default=datetime.date)),
            ],
        ),
    ]
