from django.db import models


class Rower(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    height_ft = models.PositiveSmallIntegerField()
    height_in = models.PositiveSmallIntegerField()
# Create your models here.
