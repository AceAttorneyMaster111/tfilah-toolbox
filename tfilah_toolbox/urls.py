"""tfilah_toolbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path("hashirim_shelanu/", include("hashirim_shelanu.urls")),
    path("service_generator/", include("service_generator.urls")),
    path("admin/", admin.site.urls),
    path("", views.index),
    path("login", LoginView.as_view(template_name="tfilah_toolbox/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
