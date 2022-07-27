from django import template
from app_search.models import Manga
from app_manga.models import Genre
from random import randrange

register = template.Library()

@register.inclusion_tag("app_manga/latest_manga.html")
def latest_5_manga(*args):
    return {"latest_manga": Manga.manga_latest(0,5)}

@register.simple_tag
def get_random_genre():
    genre_len = Genre.objects.values('id_genre').count()
    random_id = randrange(1, genre_len+1)
    return random_id

@register.inclusion_tag("app_manga/staffs_favorites.html")
def get_staff_favorites(*args):
    ids = [1,3]
    return {"staff": Manga.objects.filter(id_manga__in=ids).values('id_manga', 'name')}
