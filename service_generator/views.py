from django.http import HttpResponse
from django.shortcuts import render

def search(request):
    return HttpResponse("You are on the search page.")

def viewfile(request, song_id):
    return HttpResponse(f"You are looking at song {song_id}.")