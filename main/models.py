from django.db import models
from django.contrib.auth.models import User


def str_obj(user):
    return user.email


User.__str__ = str_obj


class Person(User):
    picture = models.CharField(max_length=255, null=True, blank=True)
    fb_id = models.CharField(max_length=255, null=True, blank=True)
