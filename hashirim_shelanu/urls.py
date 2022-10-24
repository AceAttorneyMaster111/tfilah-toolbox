from django.urls import path

from . import views

app_name = "hashirim_shelanu"
urlpatterns = [
    path("", views.search, name="search"),
    path("filter/", views.search_filter, name="filter"),
    path("viewsong/<int:song_id>/", views.viewsong, name="viewsong"),
    path("viewsong/<int:song_id>/download_chordpro/", views.download_chordpro, name="download_chordpro"),
    path("viewsong/<int:song_id>/download_pdf/", views.download_pdf, name="download_pdf"),
    path("viewartist/<int:artist_id>/", views.viewartist, name="viewartist"),
    path("viewprayer/<int:prayer_id>/", views.viewprayer, name="viewprayer"),
]
