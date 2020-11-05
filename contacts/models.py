from django.contrib.auth.models import User
from django.db import models


class Names(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    savedUsers = models.ManyToManyField(User, blank=True)
    nameList = models.ManyToManyField(Names)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    isSpam = models.BooleanField(default=False)

    def __str__(self):
        return self.phone
