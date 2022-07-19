from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.landing, name="landing"),
    path("viewservicetype/<int:service_id>", views.view_service_type, name="view_service_type")
]