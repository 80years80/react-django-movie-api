from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=255)
    openingText = models.CharField(max_length=255)
    releaseDate = models.DateField()