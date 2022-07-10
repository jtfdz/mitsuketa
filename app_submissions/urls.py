from django.urls import path
from . import views

urlpatterns = [
    path('send_submissions/', views.send_submissions, name='send_submissions'),
]
