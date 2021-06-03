from django.http import HttpResponse
from django.shortcuts import render

from .models import Song

def search(request):
    return render(request, "service_generator/search.html", {"song_list": Song.objects.all})

def viewsong(request, song_id):
    return HttpResponse(f"You are looking at song {song_id}.")