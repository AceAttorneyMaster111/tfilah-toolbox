from django.shortcuts import render

from .models import Service_Type

# Create your views here.
def landing(request):
    return render(request, "service_generator/landing.html", {"service_types": Service_Type.objects.all})

def create_service(request, service_id):
    pass