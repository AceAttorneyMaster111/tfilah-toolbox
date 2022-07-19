from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("viewservicetype/<int:service_id>", views.view_service_type, name="view_service_type"),
    path("", views.landing, name="landing"),
    path("createservice/<int:service_id>", views.create_service, name="create_service")
]