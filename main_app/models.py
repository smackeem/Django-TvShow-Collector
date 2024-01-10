from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length = 100)
    network = models.CharField(max_length = 10)
    run = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 100)
    season = models.IntegerField()