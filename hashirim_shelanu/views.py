from chopro import chopro2html

from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render

from .models import Artist, Prayer, Song

def search(request):
    return render(request, "hashirim_shelanu/search.html",
        {"song_list": Song.objects.all, "filter_text": "", "order_by": "title", "select": {
            "title": True,
            "artist": False,
            "prayer": False
        }, "include_tags": False})

def filter(request):
    filter_by = {
        "title": "filter_by_title" in request.GET,
        "artist": "filter_by_artist" in request.GET,
        "prayer": "filter_by_prayer" in request.GET
    }
    if not filter_by["title"] and not filter_by["artist"] and not filter_by["prayer"]:
        filter_by["title"] = filter_by["artist"] = filter_by["prayer"] = True

    filter_text = request.GET["filter_text"]
    query = ((Q(title__icontains=filter_text) | (Q(tags__name__icontains=filter_text) if "include_tags" in request.GET else Q()) if filter_by["title"] else Q())
        | (Q(artist__name__icontains=filter_text) if filter_by["artist"] else Q())
        | (Q(prayer__name__icontains=filter_text) | (Q(prayer__tags__name__icontains=filter_text) if "include_tags" in request.GET else Q()) if filter_by["prayer"] else Q())
    )
    song_list = Song.objects.filter(query).distinct().order_by(request.GET["order_by"])

    return render(request, "hashirim_shelanu/search.html",
        {"song_list": song_list, "filter_text": filter_text, "order_by": request.GET["order_by"], "select": filter_by, "include_tags": "include_tags" in request.GET})

def viewsong(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.chordsheet.file.open("r")
    chordsheet_html = chopro2html(song.chordsheet.file.read())
    song.chordsheet.file.close()
    return render(request, "hashirim_shelanu/viewsong.html", {"song": song, "chordsheet_html": chordsheet_html})

def download_chordpro(request, song_id):
    return FileResponse(get_object_or_404(Song, pk=song_id).chordsheet.file, as_attachment=True)

def download_pdf(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return FileResponse(song.chordsheet.get_pdf(), as_attachment=True, filename=song.title + "_" + song.artist.name + ".pdf")

def viewartist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, "hashirim_shelanu/viewartist.html", {"artist": artist})

def viewprayer(request, prayer_id):
    prayer = get_object_or_404(Prayer, pk=prayer_id)
    return render(request, "hashirim_shelanu/viewprayer.html", {"prayer": prayer})