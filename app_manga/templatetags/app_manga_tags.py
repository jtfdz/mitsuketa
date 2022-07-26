from django import template
from app_search.models import Manga

register = template.Library()

@register.inclusion_tag("app_manga/latest_manga.html")
def latest_5_manga(*args):
    return {"latest_manga": Manga.manga_latest(0,5)}
