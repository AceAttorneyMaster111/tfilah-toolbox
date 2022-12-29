from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.landing, name="landing"),
    path("beginservice/<int:service_id>", views.begin_service, name="begin_service"),
    path("viewservicetype/<int:service_id>", views.view_service_type, name="view_service_type"),
    path("generatetemplate", views.generate_template, name="generate_template"),
    path("startnextsection", views.start_next_section, name="start_next_section")
]
