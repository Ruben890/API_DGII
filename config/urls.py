from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API DGII(no oficial)",
        default_version='v1',
        description="Esta API se encarga de descargar un archivo en formato TXT de la Dirección General de Impuestos Internos (DGII) y posteriormente lo procesa para almacenar su contenido en una base de datos.",
        terms_of_service="https://github.com/Ruben890/API_DGII/tree/main/APIDGII",
        license=openapi.License(name="Darlin Ruben Nina C." ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('APIDGII.api.routers')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

