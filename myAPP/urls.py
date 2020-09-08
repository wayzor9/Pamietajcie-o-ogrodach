from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from myAPP.api import router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api-auth/", include("rest_framework.urls")),
    path("plants/api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
