from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model as user_model
#User = user_model()

class User(AbstractUser):
    is_club = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Club(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.User.username

class Teacher(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.User.username

class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def building_name(self):
        return self.building.name

    def __str__(self):
        return self.number

class Permissionform(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=500)
    dates = models.DateField()

    def club_name(self):
        return self.club.User

    def room_number(self):
        return self.room.number

    def building_name(self):
        return self.room.building.name

    def __str__(self):
        return (self.purpose +' '+ str(self.dates))

class Authorizationlist(models.Model):
    forrooms = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.forrooms.objects.all().annotate(Count())

class Authorizationform(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    purpose = models.TextField()
    dates = models.DateField()

    def __str__(self):
        return self.purpose
