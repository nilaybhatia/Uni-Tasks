from django.db import models

# Create your models here.
class LaunchData(models.Model):
    flight_number = models.PositiveSmallIntegerField()
    launch_date = models.DateTimeField()
    rocket_name = models.TextField()
    mission_patch_link = models.URLField()
