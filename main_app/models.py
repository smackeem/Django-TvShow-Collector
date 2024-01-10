from django.db import models
from django.urls import reverse

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length = 100)
    network = models.CharField(max_length = 10)
    run = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 100)
    season = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'show_id': self.id})