from django.shortcuts import render
from app_manga.models import Genre # not used yet
from .models import Manga, MangaTags, MangaHost
from .costum_modules.filters import *
from app_manga.costum_modules.home_data import random_set
from math import ceil
from random import randrange
# Create your views here.

def genres(request):
    return render(request, 'app_search/genres.html')

def manga(request, id=1):

    if id == 0:
        manga_len = Manga.objects.values('id_manga').count()
        id = randrange(1, manga_len+1)

    context = {
        'random_manga': Manga.objects.filter(id_manga__in=random_set()),
        'manga': Manga.objects.filter(id_manga=id).first(),
        'hosts': MangaHost.page_manager.filter(manga__id_manga=id).values('page__name', 'url'),
        'tags': MangaTags.tags_manager.filter(manga__id_manga=id).values('tags__name'),
    }

    return render(request, 'app_search/single_manga.html', context)

def search(request):

    qs_filter = Manga.objects.all()

    # order by filter
    ob_filter = request.GET.get('order_by')
    qs_filter = if_tag_exists(ob_filter, qs_filter, f_order_by)

    # status filter
    status_filter = request.GET.get('status')
    qs_filter = if_tag_exists(status_filter, qs_filter, f_status)

    # genre filter
    genre_filter = request.GET.get('genre')
    qs_filter = if_tag_exists(genre_filter, qs_filter, f_genre)

    # tag filter
    tags_filter = request.GET.get('tags')
    qs_filter = if_tag_exists(tags_filter, qs_filter, f_tag)

    # host filter
    host_filter = request.GET.get('host')
    qs_filter = if_tag_exists(host_filter, qs_filter, f_host)

    # input filter
    input_filter = request.GET.get('input')
    qs_filter = if_tag_exists(input_filter, qs_filter, f_input)
    entered_input = '' if input_filter is None else input_filter

    # page filter
    page_filter = request.GET.get('page')
    len_qsf = len(qs_filter)
    num_paginas = ceil(len_qsf / 20)
    qs_filter = if_tag_exists(page_filter, qs_filter, f_page)

    # search auto-complete
    manga_suggestions = Manga.objects.values('name')



    context = {
        'filters': filters,
        'manga': qs_filter,
        'num_paginas': range(num_paginas),
        'status': status_ogw,
        'entered_input': entered_input,
        'manga_suggestions': manga_suggestions,
    }


    return render(request, 'app_search/search.html', context)
