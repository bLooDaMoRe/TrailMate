from django.db import models
from catalog.models import Feature


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Trail(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    distance = models.FloatField()
    duration = models.FloatField()
    difficulty = models.CharField(max_length=20)

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    features = models.ManyToManyField(
        Feature,
        blank=True
    )

    def __str__(self):
        return self.name