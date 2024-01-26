# backend/server/server/urls.py file
from django.contrib import admin
from django.urls import path
from django.urls import re_path, include
from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
