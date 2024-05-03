from django.db import models
from django.conf import settings
from typing import Any


class UserFollows(models.Model):
    """
    Model to represent user follow relationships.
    """

    user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        """
        Meta class for UserFollows model.
        """

        unique_together = (
            "user",
            "followed_user",
        )

    def __str__(self) -> str:
        """
        String representation of the UserFollows instance.

        Returns:
            str: String representation.
        """
        return f'{self.followed_user}'
