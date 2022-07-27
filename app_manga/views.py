from django.shortcuts import render
from .models import Genre
from app_search.models import Manga
from django.contrib import messages
from app_manga.costum_modules.home_data import * # carousel and random_set()

def home(request):
    context = {
        'genres': Genre.objects.order_by('-readers')[:3],
        'random_manga': Manga.objects.filter(id_manga__in=random_set()),
        'carousel': carousel,
    }
    return render(request, 'app_manga/home.html', context)


def about(request):
    return render(request, 'app_manga/about.html')
