from django.db import models
from app_manga.models import Genre
from django.db.models import Count
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
# Create your models here.


def multiple_values_tag(cls, lista, filter_name, filter_query):
    return cls.filter(
                        **{filter_query : lista}
                    ).annotate(
                        n_tag_list=Count(filter_name)
                    ).filter(
                        n_tag_list=len(lista)
                    )

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

        # tag_id + tag_name + count of use
        def get_relevant(self):
            lista_count = self.values(self.mtp_field)\
                              .annotate(name_count=Count(self.mtp_field))\
                              .values(self.mtp_field+'__name', 'name_count', self.mtp_field)\
                              .order_by('-name_count')
            return lista_count

        # manga id + list of id tags
        def get_dictionary(self):
            tags_pages = self.values(self.mtp_field, 'manga__id_manga')
            manga_dict = {}

            for i in tags_pages:
                manga = str(i.get('manga__id_manga'))
                tag = i.get(self.mtp_field, [])
                value = manga_dict.get(manga, set())
                value.add(tag)
                manga_dict.update({manga: value})

            return manga_dict


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


    @property
    def image_previews(self):
        image_preview = []
        for p in range(1,4):
            pic_str = 'img/MANGA_PREVIEWS/MP_'+ str(self.name).replace(" ","_") + '_' + str(p) +'.jpg'
            image_preview.append(pic_str)
        return image_preview


    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return 'img/MANGA_'+ str(self.name).replace(" ","_") +'.jpg'

    @classmethod
    def manga_latest(cls, num_start=0, num_end=0):
        if num_end:
            return cls.objects.order_by('-last_update')[num_start:num_end]
        else:
            return cls.objects.order_by('-last_update')[num_start:]


class MangaHost(models.Model):
    id_manga_host = models.BigAutoField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    url = models.URLField(max_length = 250)
    page_manager = manager_factory('page')

    def __str__(self):
        return f'{self.manga}: {self.page.name} in {self.url}'




class MangaTags(models.Model):
    id_manga_tag = models.BigAutoField(primary_key=True)
    manga = models.OneToOneField(Manga, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    tags_manager = manager_factory('tags')
    def __str__(self):
        #tag_list = [i for i in self.tags.name]
        return f'{self.manga}: {self.tags.all()}'


def tags_changed(sender, **kwargs):
    if kwargs['instance'].tags.count() > 5:
        raise ValidationError("you can't assign more than five tags")

m2m_changed.connect(tags_changed, sender=MangaTags.tags.through)
