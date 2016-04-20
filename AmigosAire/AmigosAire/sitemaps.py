from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from datetime import datetime
from apps.main.models import Servicios

class VueloSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Servicios.objects.all()

    def lastmod(self,obj):
        return datetime.now()

    def location(self,obj):
        return '/plan/%s'%obj.slug

class SitesSitemap(Sitemap):
    def __init__(self,names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self,obj):
        return 'weekly'

    def lastmod(self,obj):
        return datetime.now()

    def location(self,obj):
        return reverse(obj)
