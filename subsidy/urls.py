from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'subsidy'

urlpatterns = [
    # Common information
    path('operator-information/', views.Operator_Information.as_view(), name='operator_information'),
    path('terms-of-service/', views.Terms_of_Service.as_view(), name='terms_of_service'),
    path('inquiry/', views.Inquiry_create.as_view(), name='inquiry_create'),
    path('inquiry-done/', views.Inquiry_done.as_view(), name='inquiry_done'),
    # Tokyo23
    path('', views.Tokyo23_Top.as_view(), name='tokyo23_top'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('tokyo23-index/', views.Tokyo23_Index.as_view(), name='tokyo23_index'),
    path('tokyo23-marriage/', views.Tokyo23_marriage.as_view(), name='tokyo23_marriage'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
