from django.conf import settings
from django.contrib import admin
from django.urls import include, path

BASE_API_PATH: str = getattr(settings, "BASE_API_PATH", "api")

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{BASE_API_PATH}/", include("apps.auth.urls")),
]
