from django.db import models
from django.contrib.auth.models import User


class UserPhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.URLField(max_length=255, null=True, blank=True)


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class ActivityItem(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    persisted_name = models.CharField(max_length=255)
    sets = models.IntegerField(default=0, null=True, blank=True)
    reps = models.IntegerField(default=0, null=True, blank=True)
    weight = models.FloatField(default=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity.name

    def save(self, *args, **kwargs):
        self.persisted_name = self.activity.name
        super(ActivityItem, self).save(*args, **kwargs)
