from typing import Any
from xml.etree import ElementTree

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import ServiceType

# Create your views here.


def landing(request: HttpRequest) -> HttpResponse:
    return render(request, "service_generator/landing.html", {"service_types": ServiceType.objects.all})


def begin_service(request: HttpRequest, service_id: int) -> HttpResponse:
    return render(request, "service_generator/beginservice.html", {
        "service_type": get_object_or_404(ServiceType, pk=service_id)
    })


def generate_template(request: HttpRequest, args: dict[str, Any]) -> HttpResponse:
    service = ElementTree.Element("service")


def view_service_type(request: HttpRequest, service_id: int) -> HttpResponse:
    service = get_object_or_404(ServiceType, pk=service_id)
    return render(request, "service_generator/viewservicetype.html", {"service_type": service})
