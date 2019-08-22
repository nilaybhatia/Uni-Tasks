from django.db import models

# Create your models here.
class LaunchData(models.Model):
    flight_number = models.PositiveSmallIntegerField()
    launch_date = models.DateField()
    launch_time = models.TimeField()
    rocket_name = models.TextField()
    mission_patch_link = models.URLField()

    def __str__(self):
        return self.flight_number
