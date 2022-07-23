from django.shortcuts import render
from app_manga.models import Genre # another way of saying: from the same directory
from .models import Manga, Page, Tags, MangaTags, MangaPages
# Create your views here.

def search_name_plus_count(obj_manag, name, icon):
    elements = obj_manag.get_relevant()[:15]
    search_dictionary = {}
    for n, i in enumerate(elements):
        index = f"tag_{n}"
        search_name = f"{i[name]} ({i['name_count']})"
        search_dictionary[index] = [search_name, icon]
    return search_dictionary

filters = [
    {
        'filter_name': 'order by',
        'options': {
            'order_1': ["latest", "fa-fast-forward"],
            'order_2': ["oldest", "fa-fast-backward"],
            'order_3': ["from a to z","fa-sort-alpha-asc"]
        },
    },
    {
        'filter_name': 'status by original work',
        'options': {
            'status_1': ["completed", "fa-battery-full"],
            'status_2': ["on-going", "fa-battery-three-quarters"],
            'status_3': ["hiatus","fa-battery-half"],
            'status_4': ["dropped","fa-battery-empty"]
        },
    },
    {
        'filter_name': 'tags',
        'options': search_name_plus_count(MangaTags.tags_manager, 'tags', 'fa-pen'),
    },
    {
        'filter_name': 'pages',
        'options': search_name_plus_count(MangaPages.pages_manager, 'pages', 'fa-window-restore'),
    },

]




def genres(request):
    return render(request, 'app_search/genres.html')

def search(request):
    context = {
        'genres': Genre.objects.all(),
        'filters': filters,
    }
    return render(request, 'app_search/search.html', context)
