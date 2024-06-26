# Generated by Django 3.2.9 on 2024-05-21 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_initial'),
        ('authentication', '0006_user_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(related_name='followers', through='blog.UserFollows', to=settings.AUTH_USER_MODEL, verbose_name='Follows'),
        ),
    ]
