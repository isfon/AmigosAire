from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.main import urls as main_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(main_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)