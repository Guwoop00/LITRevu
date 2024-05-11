from django.db import models
from django.conf import settings
from PIL import Image
from typing import Union


class Ticket(models.Model):
    """Model representing a ticket."""

    title: str = models.fields.CharField(max_length=128)
    description: str = models.fields.CharField(max_length=2048)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    image: Union[models.ImageField, None] = models.ImageField(null=True, blank=True)
    time_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE: tuple[int, int] = (200, 200)

    def __str__(self) -> str:
        """Return string representation of the ticket."""
        return f'{self.title}'

    def resize_image(self) -> None:
        """Resize the image to fit within the maximum size."""
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

    def save(self, *args, **kwargs) -> None:
        """Override the save method to resize the image before saving."""
        super().save(*args, **kwargs)
        self.resize_image()

    def has_been_reviewed(self) -> bool:
        """Check if the ticket has been reviewed."""
        return self.review.exists()


class Review(models.Model):
    """Model representing a review."""

    ticket: Ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name='review')
    rating: int = models.PositiveSmallIntegerField()
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    headline: str = models.CharField(max_length=128)
    body: str = models.CharField(max_length=8192, blank=True)
    time_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return string representation of the review."""
        return f'{self.headline}'
