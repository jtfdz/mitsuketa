from django.contrib import admin
from .models import Manga, Page, Tags # another way of saying: from the same directory

# Register your models here.

admin.site.register([Manga, Page, Tags])
