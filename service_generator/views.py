from chopro import chopro2html

from django.http import FileResponse
from django.shortcuts import get_object_or_404, render

from .models import Song

def search(request):
    return render(request, "service_generator/search.html", {"song_list": Song.objects.all})

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