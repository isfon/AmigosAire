from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.main import urls as main_urls
from .sitemaps import SitesSitemap, VueloSitemap

sitemaps = {
    'planes':VueloSitemap,
    'pages':SitesSitemap(['index', 'faq', 'privacidad'])
}


urlpatterns = [
    url(r'^sitemap\.xml','django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(main_urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
]
