from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings

from .sitemaps import (
    SubsidySitemap,
    StaticViewSitemap,
)

sitemaps = {
    'blog': SubsidySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', include('subsidy.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
#    path('register/', include('register.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
