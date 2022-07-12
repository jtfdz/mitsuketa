from django.shortcuts import render
from .models import Genre # another way of saying: from the same directory
from django.contrib import messages
from random import choice
from app_search.models import Manga

carousel = [
    {
    'image': 'img/banner_img_00.png',
    'title': 'read: Mecha',
    'subtitle': 'put it in rice',
    'description': 'tall microwaves fighting',
    'class': 'carousel-item active',
    },
    {
    'image': 'img/banner_img_02.png',
    'title': 'read: Death Note',
    'subtitle': '2003, Tsugumi Ōba + Takeshi Obata',
    'description': "Death Note follows a high school student who comes across a supernatural notebook, realizing it holds within it a great power; if the owner inscribes someone's name into it while picturing their face, he or she will die.",
    'class': 'carousel-item',
    },
    {
    'image': 'img/banner_img_03.png',
    'title': 'read: Funny',
    'subtitle': 'knock knock',
    'description': 'so you want to laugh?',
    'class': 'carousel-item',
    },
    {
    'image': 'img/banner_img_04.png',
    'title': 'read: Dr. Stone',
    'subtitle': '2017, Riichiro Inagaki + Boichi',
    'description': "In the modern world, every human on the planet was turned into stone after a mysterious flash of light. This manga tells the story of how some people from the Pre-Petrification World try to rebuild civilization in the Petrification Age, the Stone World.",
    'class': 'carousel-item',
    },
]





def home(request):

    context = {
        'genres': Genre.objects.order_by('-readers')[:3],
        'random_manga': Manga.objects.all()[:3],
        'carousel': carousel,
    }
    return render(request, 'app_manga/home.html', context)



def about(request):
    return render(request, 'app_manga/about.html')
