from chopro import chopro2html

from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render

from .models import Song

def search(request):
    return render(request, "service_generator/search.html", {"song_list": Song.objects.all, "filter_text": ""})

def filter(request):
    filter_by = {
        "title": "filter_by_title" in request.GET,
        "artist": "filter_by_artist" in request.GET,
        "prayer": "filter_by_prayer" in request.GET
    }
    if not any(filter_by):
        filter_by["title"] = filter_by["artist"] = filter_by["prayer"] = True

    filter_text = request.GET["filter_text"]
    query = ((Q(title__icontains=filter_text) if filter_by["title"] else Q())
        | (Q(artist__icontains=filter_text) if filter_by["artist"] else Q())
        | (Q(prayer__name__icontains=filter_text) if filter_by["prayer"] else Q())
    )
    song_list = Song.objects.filter(query)

    return render(request, "service_generator/search.html", {"song_list": song_list, "filter_text": filter_text})

def viewsong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.chordsheet.open("r")
    chordsheet_html = chopro2html(song.chordsheet.read())
    song.chordsheet.close()
    return render(request, "service_generator/viewsong.html", {"song": song, "chordsheet_html": chordsheet_html})

def download_chordpro(request, song_id):
    return FileResponse(get_object_or_404(Song, pk=song_id).chordsheet, as_attachment=True)

def download_pdf(request, song_id):
    pass