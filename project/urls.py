from django.contrib import admin
from django.urls import path, include
from django.conf import settings

admin.site.site_title = 'MANAGEMENT SCREEN'
admin.site.site_header = 'MANAGEMENT SCREEN'
admin.site.index_title = 'DATABASE_LIST'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subsidy/', include('subsidy.urls')),
#   hide register app  
#   path('register/', include('register.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
