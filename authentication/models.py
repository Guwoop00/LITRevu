from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""

    username: models.CharField = models.CharField(max_length=150, unique=True)
    follows: models.ManyToManyField = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='Follows',
        related_name='followers',
        through='blog.UserFollows'
    )
