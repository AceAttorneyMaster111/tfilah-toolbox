from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.search, name="search"),
    path("viewsong/<int:song_id>/", views.viewsong, name="viewsong"),
    path("viewsong/<int:song_id>/download_chordpro/", views.download_chordpro, name="download_chordpro"),
    path("viewsong/<int:song_id>/download_pdf/", views.download_pdf, name="download_pdf")
]