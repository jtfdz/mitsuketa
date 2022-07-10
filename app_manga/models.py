from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    id_genre = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    readers = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return 'img/GENRE_'+ str(self.id_genre) +'.jpg'
