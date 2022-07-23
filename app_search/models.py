from django.db import models
from app_manga.models import Genre
from django.db.models import Count
from django.db.models.signals import m2m_changed
# Create your models here.


class Tags(models.Model):
    id_tag = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Page(models.Model):
    id_page = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

def manager_factory(custom_field):
    class SearchManager(models.Manager):
        mtp_field = custom_field # manga tags/page

        def get_relevant(self):
            # ex: [{tags: 1, name_count=2}, ...]
            list_count = self.values(self.mtp_field)\
                       .annotate(name_count=Count(self.mtp_field))\
                       .order_by('-name_count')
            # ex: [1, 3, 4, 6]
            list_ids = [i[self.mtp_field] for i in list_count]
            # puede ser simplificado con *args, etc
            for a,b in zip(list_count, list_ids):
                if self.mtp_field == 'tags':
                    clean_a = self.filter(tags__id_tag=b).values('tags__name').distinct()
                    a[self.mtp_field] = clean_a[0]['tags__name']
                else:
                    clean_a = self.filter(pages__id_page=b).values('pages__name').distinct()
                    a[self.mtp_field] = clean_a[0]['pages__name']
            return list_count


    return SearchManager()


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
    volumes = models.PositiveIntegerField()
    status = models.CharField(choices = STATUS_CHOICES, max_length=10)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return 'img/MANGA_'+ str(self.name).replace(" ","_") +'.jpg'

    @classmethod
    def manga_latest(cls):
        return cls.objects.order_by('-last_update')[:5]




class MangaTags(models.Model):
    id_manga_tag = models.BigAutoField(primary_key=True)
    manga = models.OneToOneField(Manga, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    tags_manager = manager_factory('tags')
    def __str__(self):
        #tag_list = [i for i in self.tags.name]
        return f'{self.manga}: {self.tags.all()}'

class MangaPages(models.Model):
    id_manga_tag = models.BigAutoField(primary_key=True)
    manga = models.OneToOneField(Manga, on_delete=models.CASCADE)
    pages = models.ManyToManyField(Page)
    pages_manager = manager_factory('pages')
    def __str__(self):
        #tag_list = [i for i in self.tags.name]
        return f'{self.manga}: {self.pages.all()}'

def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 5:
        raise ValidationError("you can't assign more than five tags")

m2m_changed.connect(tags_changed, sender=MangaTags.tags.through)
