import io
from typing import Optional
from xml.etree import ElementTree

from django.http import HttpRequest, HttpResponse, FileResponse
from django.shortcuts import get_object_or_404, render

from .models import ServiceType, ServiceTypeSection


# Create your views here.


def landing(request: HttpRequest) -> HttpResponse:
    return render(request, "service_generator/landing.html", {"service_types": ServiceType.objects.all})


def begin_service(request: HttpRequest, service_id: int) -> HttpResponse:
    return render(request, "service_generator/beginservice.html", {
        "service_type": get_object_or_404(ServiceType, pk=service_id)
    })


def generate_template(request: HttpRequest, service_id: int) -> HttpResponse:
    title = request.POST["title"]
    service = ElementTree.Element("service")
    metadata = ElementTree.SubElement(service, "metadata")
    # noinspection PyTypeChecker
    metadata.extend([
        ElementTree.Element("servicetype", text=ServiceType.objects.get(id=service_id)),
        ElementTree.Element("occasion", text=request.POST.get("occasion", "")),
        ElementTree.Element("community", text=request.POST.get("community", "")),
        ElementTree.Element("theme", text=request.POST.get("theme", "")),
        ElementTree.Element("mood", text=request.POST.get("mood", "")),
        ElementTree.Element("time", text=request.POST.get("time", "")),
        ElementTree.Element("parashah", text=request.POST.get("parashah", "")),
        ElementTree.Element("space", text=request.POST.get("space", ""))
    ])
    style = ElementTree.SubElement(metadata, "style")
    # TODO add style
    request.session["service"] = service
    request.session["service_title"] = title
    return start_next_section(request, service_id, 1)


def start_next_section(request: HttpRequest, service_id: int, next_section: int) -> HttpResponse:
    if len((service_type := ServiceType.objects.get(id=service_id)).sections) < next_section:
        return finalize_service(request)
    service = request.session["service"]
    section = service_type.sections[next_section]
    service.append(ElementTree.Element("section", {"name": section.display_name}))
    return next_element(request, service_id, next_section, 1)


def _next_prayer(service_type: ServiceType, section_index: int, prayer_index: int) -> tuple[Optional[str], Optional[str]]:
    """Return the name of the next prayer. If that prayer is in a new section, return the name of that section too."""
    if len(service_type.sections[section_index].prayers) > prayer_index:
        # Next prayer is in this section
        return None, service_type.sections[section_index].prayers[prayer_index + 1].name
    if len(service_type.sections) > section_index:
        # Go to next section
        return service_type.sections[section_index + 1].name, service_type.sections[section_index + 1].prayers[1].name
    # Finalize
    return None, None


def next_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    if len((service_type := ServiceType.objects.get(id=service_id)).sections[section_index].prayers) < prayer_index:
        return start_next_section(request, service_id, section_index + 1)
    return render(request, "service_generator/nextelement.html", {
        "service_type": service_type,
        "section": (section_ := service_type[section_index]),
        "prayer": section_[prayer_index],
        "next_prayer_name": _next_prayer(service_type, section_index, prayer_index)
    })


def add_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    if not request.POST["element_type"]:
        return next_element(request, service_id, section_index, prayer_index + 1)
    return render(request, f"service_generator/add{request.POST['element_type']}element", {
        "service_type": (service_type := ServiceType.objects.get(id=service_id)),
        "section": (section_ := service_type[section_index]),
        "prayer": section_[prayer_index]
    })


def add_song_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    service = request.session["service"]
    curr_section = service[-1]
    new_element = ElementTree.SubElement(curr_section, "element", {"type": "song", "id": request.POST["song_id"]})
    new_element.extend([

    ])
    return next_element(request, service_id, section_index, prayer_index)


def add_prayer_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    # TODO
    return next_element(request, service_id, section_index, prayer_index)


def add_reading_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    # TODO
    return next_element(request, service_id, section_index, prayer_index)


def add_iyun_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    # TODO
    return next_element(request, service_id, section_index, prayer_index)


def add_other_element(request: HttpRequest, service_id: int, section_index: int, prayer_index: int) -> HttpResponse:
    # TODO
    return next_element(request, service_id, section_index, prayer_index)


def finalize_service(request: HttpRequest) -> HttpResponse:
    service = request.session["service"]
    title = request.session["service_title"]
    del request.session["service"]
    del request.session["service_title"]
    return render(request, "service_generator/viewservice.html", {"service": service, "service_title": title})


def download_xml(request: HttpRequest, service: str, title: str) -> FileResponse:
    xml = ElementTree.fromstring(service)
    tree = ElementTree.ElementTree(xml)
    buffer = io.BytesIO()
    tree.write(buffer, "utf-8", True)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{title}.xml")


def download_pdf(request: HttpRequest, service: str, title: str) -> FileResponse: pass


def upload_xml(request: HttpRequest) -> HttpResponse:
    # TODO work file magic
    service, title = None
    return render(request, "service_generator/viewservice.html", {"service": service, "service_title": title})


def view_service_type(request: HttpRequest, service_id: int) -> HttpResponse:
    service = get_object_or_404(ServiceType, pk=service_id)
    return render(request, "service_generator/viewservicetype.html", {"service_type": service})


def view_section(request: HttpRequest, service_type_section_id: int) -> HttpResponse:
    service_type_section = get_object_or_404(ServiceTypeSection, pk=service_type_section_id)
    return render(request, "service_generator/viewsection.html", {"service_type_section": service_type_section})