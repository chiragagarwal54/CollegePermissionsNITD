from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model as user_model
#User = user_model()

class authorization_list():
    for_rooms = models.ManyToManyField(User, on_delete=models.CASCADE)

class authorization_form():
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    purpose = models.TextField()
    dates = models.DateField()
    
