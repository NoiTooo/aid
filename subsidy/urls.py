from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'subsidy'

urlpatterns = [
    path('', views.CountDown.as_view(), name='countdown'),
    # Common information
    path('about-service/', views.About_Service.as_view(), name='about_service'),
    path('webmaster/', views.Webmaster.as_view(), name='webmaster'),
    path('terms-of-service/', views.Terms_of_Service.as_view(), name='terms_of_service'),
    path('user-alert/', views.User_Alert.as_view(), name='user_alert'),
    path('user-alert-done/', views.User_Alert_Done.as_view(), name='user_alert_done'),
    path('inquiry/', views.Inquiry_Create.as_view(), name='inquiry_create'),
    path('inquiry-done/', views.Inquiry_Done.as_view(), name='inquiry_done'),
    # Tokyo23
    path('tokyo23/', views.Tokyo23_Top.as_view(), name='tokyo23_top'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('tokyo23-index/', views.Tokyo23_Index.as_view(), name='tokyo23_index'),
    path('tokyo23-category/', views.Tokyo23_Category_Select.as_view(), name='tokyo23_category_select'),
    path('tokyo23-marriage/', views.Tokyo23_marriage.as_view(), name='tokyo23_marriage'),
    path('tokyo23-housing/', views.Tokyo23_Housing.as_view(), name='tokyo23_housing'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
