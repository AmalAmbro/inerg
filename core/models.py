from django.db import models

# Create your models here.
class Well(models.Model):
    well = models.CharField(max_length=150, primary_key=True)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __str__(self):
        return f"{self.well}"