"""Models for the resources application."""

from django.db import models


class Resource(models.Model):
    """Model for resource in database."""

    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    webpage_template = models.CharField(max_length=200)
    generation_view = models.CharField(max_length=200)
    thumbnail_static_path = models.CharField(max_length=200)

    def __str__(self):
        """Text representation of Resource object.

        Returns:
            Name of resource (string).
        """
        return self.name