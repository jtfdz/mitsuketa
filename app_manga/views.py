from django.shortcuts import render
from .models import Genre # another way of saying: from the same directory

random_manga = [
    {
    'id_manga': '1',
    'name': 'snk',
    'description': 'AND FUCK ZEKE!',
    'reviews': 391484223,
    'main_genre': 'shounen',
    },
    {
    'id_manga': '23342',
    'name': 'tamen de gushi',
    'description': 'love exists T__T',
    'reviews': 1271,
    'main_genre': 'romance',
    },
    {
    'id_manga': '5934',
    'name': 'therapy game ♥',
    'description': 'not a single therapy session in sight',
    'reviews': 554,
    'main_genre': 'romance',
    }
]

def home(request):
    context = {
        'genres': Genre.objects.all(),
        'random_manga': random_manga,
    }
    return render(request, 'app_manga/home.html', context)



def about(request):
    return render(request, 'app_manga/about.html')
