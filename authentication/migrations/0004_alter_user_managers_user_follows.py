# Generated by Django 5.0.4 on 2024-04-26 00:19

import django.contrib.auth.models
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_remove_user_profile_photo_alter_user_username"),
        ("blog", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("feed_manager", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(
                related_name="followers",
                through="blog.UserFollows",
                to=settings.AUTH_USER_MODEL,
                verbose_name="suit",
            ),
        ),
    ]
