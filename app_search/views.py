from django.shortcuts import render
from app_manga.models import Genre # another way of saying: from the same directory

# Create your views here.

"""
def genre(request, pk):
    return render(request, 'app_search/genre.html')
"""

def genres(request):
    return render(request, 'app_search/genres.html')

def search(request):
    return render(request, 'app_search/search.html')
