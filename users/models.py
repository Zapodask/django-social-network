from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Friends(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="friends",
    )
    users = models.ManyToManyField(
        User,
        related_name="users",
    )
