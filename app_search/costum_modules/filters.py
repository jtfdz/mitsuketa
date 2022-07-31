from app_manga.models import Genre
from ..models import Manga, MangaTags, MangaHost, multiple_values_tag
from django.db.models import Q
from math import ceil

# formatting for tags w multiple values
def get_filters(obj_manag, name, icon, genres):
    elements = obj_manag.all() if genres else obj_manag.get_relevant()[:15]

    search_dictionary = {}
    for n, i in enumerate(elements, 1):
        index = f"{name}_{n}" if genres else f"{name}_{i[name]}"
        search_name = f"{i.name}" if genres else f"{i[name+'__name']} ({i['name_count']})"
        search_dictionary[index] = [search_name, icon]


    return search_dictionary

# status by original work
status_ogw = [
    ["completed", "fa-battery-full"],
    ["on-going", "fa-battery-three-quarters"],
    ["hiatus","fa-battery-half"],
    ["dropped","fa-battery-empty"]
]

# all filters format
filters = [
    {
        'filter_name': 'order by',
        'options': {
            'order_1': ["latest", "fa-fast-forward"],
            'order_2': ["oldest", "fa-fast-backward"],
            'order_3': ["from a to z","fa-info"],
        },
        'filter_form': 'order_by'
    },
    {
        'filter_name': 'genre',
        'options': get_filters(Genre.objects, 'genres', 'fa-tag', True),
        'filter_form': 'genre'
    },
    {
        'filter_name': 'status by original work',
        'options': {
            'completed': status_ogw[0],
            'on-going': status_ogw[1],
            'hiatus': status_ogw[2],
            'dropped': status_ogw[3],
        },
        'filter_form': 'status'
    },
    {
        'filter_name': 'tags',
        'options': get_filters(MangaTags.tags_manager, 'tags', 'fa-pen', False),
        'filter_form': 'tags'
    },
    {
        'filter_name': 'host pages',
        'options': get_filters(MangaHost.page_manager, 'page', 'fa-window-restore', False),
        'filter_form': 'host'
    },
]


# order-by filter
def f_order_by(tag, qs):
    order = {
        'order_1': '-last_update',
        'order_2': 'last_update',
        'order_3': 'name',
    }

    get_order = order.get(tag, order['order_1'])
    return qs.order_by(get_order)

# status filter
def f_status(tag, qs):
    for s in status_ogw:
        if tag == s[0]:
            return qs.filter(status=tag)

# filters w multiple values
def n_tags_ids(tag):
    tag = tag.split('-')
    clean_tag = [t.split("_")[1] for t in tag]
    set_ids = {int(t) for t in clean_tag}
    return set_ids

# genre filter
def f_genre(tag, qs):
    ids = n_tags_ids(tag)
    return multiple_values_tag(qs, ids, 'genres__id_genre', 'genres__in')

# tag and host filter share exactly the same code but different manager_factory
def f_tage(obj_man, tag, qs):

    ids = n_tags_ids(tag)
    manga_dict = obj_man.get_dictionary()
    accepted_manga_ids = []

    for key, value in manga_dict.items():
        if ids.issubset(value):
            accepted_manga_ids.append(key)


    return qs.filter(id_manga__in=accepted_manga_ids)

# tag filter
def f_tag(tag, qs):
    return f_tage(MangaTags.tags_manager, tag, qs)

# host filter
def f_host(tag, qs):
    return f_tage(MangaHost.page_manager, tag, qs)

# input filter
def f_input(tag, qs):
    filter_fields = qs.filter(Q(name__contains=tag) | Q(description=tag) | Q(author=tag))
    return filter_fields

# page filter
def f_page(tag, qs):
    num_pag = int(tag)
    first_num = 0 if num_pag == 1 else (num_pag)*20
    last_num = 21 if num_pag == 1 else first_num+21
    return qs[first_num:last_num]

# check if tag is requested
def if_tag_exists(tag, qs, fc):
    if tag is not None and tag != '':
        return fc(tag, qs)
    else:
        return qs
