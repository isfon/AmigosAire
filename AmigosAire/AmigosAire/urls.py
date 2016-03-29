from django.conf.urls import url, include
from django.contrib import admin
from apps.main import urls as main_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(main_urls)),
]