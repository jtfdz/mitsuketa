from django.db import models
from app_manga.models import Genre
from django.db.models.signals import m2m_changed
# Create your models here.

class Tags(models.Model):
    id_tags = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


STATUS_CHOICES = (("completed", "completed"),
                 ("on-going", "on-going"),
                 ("hiatus", "hiatus"),
                 ("dropped", "dropped"))

class Manga(models.Model):
    id_manga = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    clicks = models.PositiveIntegerField() # suma al genre
    genres = models.ManyToManyField(Genre)
    author = models.CharField(max_length=100)
    last_update = models.DateField(auto_now=True)
    chapters = models.PositiveIntegerField()
    status = models.CharField(choices = STATUS_CHOICES, max_length=10)
    emoji = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return 'img/MANGA_'+ str(self.id_manga) +'.jpg'


class Page(models.Model):
    id_page = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    manga_offered = models.ManyToManyField(Manga)



def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 5:
        raise ValidationError("you can't assign more than five tags")

m2m_changed.connect(tags_changed, sender=Manga.tags.through)
