from gm2m import GM2MField

from django.db import models
from django.contrib.auth.models import User

from .managers import AnnouncentManager

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=180, blank=False, null=False, unique=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name


class Announcement(models.Model):
    header = models.CharField(max_length=50, blank=True, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    views = GM2MField()
    views_count = models.PositiveIntegerField(default=0)

    objects = AnnouncentManager()

    def __str__(self):
        return self.header or self.description