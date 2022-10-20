from django.shortcuts import get_object_or_404, render

from .models import ServiceType

# Create your views here.
def landing(request):
    return render(request, "service_generator/landing.html", {"service_types": Service_Type.objects.all})

def view_service_type(request, service_id):
    service = get_object_or_404(Service_Type, pk=service_id)
    return render(request, "service_generator/viewservicetype.html", {"service_type": service})