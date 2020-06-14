from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'subsidy'

urlpatterns = [
    path('inquiry/', views.Inquiry_create.as_view(), name='inquiry_create'),
    path('inquiry-done/', views.Inquiry_done.as_view(), name='inquiry_done'),
    path('', views.Tokyo23_Top.as_view(), name='tokyo23_top'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('tokyo23-marriage/', views.Tokyo23_marriage.as_view(), name='tokyo23_marriage'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
