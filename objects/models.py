from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    centre = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.number

class Permissionform(models.Model):
    club = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    dates = models.DateField()
    purpose = models.CharField(max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return (self.purpose +' '+ str(self.dates))
