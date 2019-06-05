from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class room(models.Model):
    name = models.ForeignKey(building, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.name
