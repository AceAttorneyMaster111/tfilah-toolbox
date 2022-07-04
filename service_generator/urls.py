from django.urls import path

from . import views

app_name = "service_generator"
urlpatterns = [
    path("", views.landing, name="landing")
]