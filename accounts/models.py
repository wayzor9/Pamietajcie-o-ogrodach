from django.contrib.auth.models import AbstractUser
from django.db import models

from plants.models import Plant, ProfilePlant
from .managers import UserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, max_length=200)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class UserProfile:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plant = models.ManyToManyField(Plant, through=ProfilePlant)
    # weather = models.ForeignKey(User, on_delete=models.CASCADE)
    # location
