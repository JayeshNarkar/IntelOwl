# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0015_visualizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='received_request_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
