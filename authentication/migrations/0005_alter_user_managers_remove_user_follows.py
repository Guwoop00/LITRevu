# Generated by Django 5.0.4 on 2024-04-26 00:33

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_alter_user_managers_user_follows"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="follows",
        ),
    ]
