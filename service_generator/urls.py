from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.landing, name="landing"),
    path("createservice/<int:service_id>", views.create_service, name="create_service")
]