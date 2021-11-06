from django.db import models


class SensorRecord(models.Model):
    date_recorded = models.DateTimeField()
    value = models.IntegerField()

    def __str__(self):
        return str(self.date_recorded)
