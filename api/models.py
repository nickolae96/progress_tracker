from django.db import models
from django.contrib.auth.models import User


class UserPhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.URLField(max_length=255, null=True, blank=True)
