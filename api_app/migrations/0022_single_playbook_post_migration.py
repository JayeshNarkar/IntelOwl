# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-27 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0021_single_playbook_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='playbooks_requested',
        ),
        migrations.RemoveField(
            model_name='job',
            name='playbooks_to_execute',
        ),
        migrations.AlterField(
            model_name='job',
            name='playbook_requested',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_in_jobs', to='playbooks_manager.playbookconfig'),
        ),
        migrations.AlterField(
            model_name='job',
            name='playbook_to_execute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executed_in_jobs', to='playbooks_manager.playbookconfig'),
        ),
    ]
