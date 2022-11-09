from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.views import LoginView

from .views import EmployeeListView

schema_view = get_schema_view(
    openapi.Info(
        title="Multi Tenant API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("api/v1/", include("company.urls")),
    # path("", include("django.contrib.auth.urls")),
    path("", LoginView.as_view(), {"template_name": "login.html"}),
    path("employee-list/", EmployeeListView.as_view(), name="employee-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
