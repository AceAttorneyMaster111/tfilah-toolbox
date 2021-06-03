from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.search, name="search"),
    path("viewsong/<int:song_id>/", views.viewsong, name="viewsong")
]