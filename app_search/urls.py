from django.urls import path
from . import views

urlpatterns = [
    path('genres', views.genres, name='genres'),
    #path('genre/<int:pk>', views.genre, name='genre'),
    path('search/', views.search, name='search'), # filter and so on
]
