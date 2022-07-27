from django.urls import path, re_path
from . import views

urlpatterns = [
    path('genres', views.genres, name='genres'),
    #path('genre/<int:pk>', views.genre, name='genre'),
    path('manga/<int:id>', views.manga, name='manga'),
    path('search/', views.search, name='search'), # filter and so on
    re_path(r'''^search/
            (?:page=(?P<page>[0-9]{5}\d+)/)
            (?:order_by=(?P<order_by>\d+)/)
            (?:genre=(?P<genre>\d+)/)
            (?:status=(?P<status>\d+)/)
            (?:tags=(?P<tags>\d+)/)
            (?:host=(?P<host>\d+)/)
            (?:input=(?P<input>\d+)/)''', views.search, name='search'),
]


"""
    path('search/order_by=<str:order_by>/', views.search, name='search'),

"""
