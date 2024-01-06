from django.contrib import admin
from api import models


admin.site.register(models.UserPhoto)
admin.site.register(models.Activity)
admin.site.register(models.ActivityItem)
