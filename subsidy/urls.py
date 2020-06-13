from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'subsidy'

urlpatterns = [
    path('', views.Tokyo23_Top.as_view(), name='tokyo23_top'),
    path('tokyo23-marriage/', views.Tokyo23_Marriage.as_view(), name='tokyo23_marriage'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
