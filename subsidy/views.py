from datetime import datetime

from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from subsidy.models import Subsidy, City, Prefecture, Theme
from .forms import InquiryCreateForm, UserAlertForm


"""
共通情報
"""


class Operator_Information(generic.TemplateView):
    """運営者情報"""
    template_name = 'subsidy/common_information/operator_information.html'


class Terms_of_Service(generic.TemplateView):
    """利用規約"""
    template_name = 'subsidy/common_information/terms_of_service.html'


class User_Alert(generic.CreateView):
    """ユーザーアラート"""
    template_name = 'subsidy/common_information/user_alert.html'
    form_class = UserAlertForm
    success_url = reverse_lazy('subsidy:user_alert_done')


class User_Alert_Done(generic.TemplateView):
    """ユーザーアラート入力完了"""
    template_name = 'subsidy/common_information/user_alert_done.html'


class Inquiry_Create(generic.CreateView):
    """問い合わせフォーム"""
    template_name = 'subsidy/common_information/inquiry_create.html'
    form_class = InquiryCreateForm
    success_url = reverse_lazy('subsidy:inquiry_done')


class Inquiry_Done(generic.TemplateView):
    """問い合わせ完了"""
    template_name = 'subsidy/common_information/inquiry_done.html'


"""
東京都23区版
"""


class Tokyo23_Top(generic.TemplateView):
    """TOPページ"""
    template_name = 'subsidy/tokyo23/tokyo23_top.html'


class Detail(generic.DeleteView):
    """案件詳細ページ"""
    template_name = 'subsidy/common_information/detail.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object'


class Tokyo23_Index(generic.ListView):
    """23区の制度一覧"""
    template_name = 'subsidy/tokyo23/tokyo23_index.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'

    def get_queryset(self):
        return Subsidy.objects.filter(is_published=True, prefectures__prefecture='東京都23区')


class Tokyo23_marriage(generic.ListView):
    """テーマ「結婚」"""
    template_name = 'subsidy/tokyo23/tokyo23_marriage.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'

    def get_queryset(self):
        return Subsidy.objects.filter(is_published=True, prefectures__prefecture='東京都23区', themes__theme='結婚')

class Tokyo23_Housing(generic.ListView):
    """テーマ「住まい」"""
    template_name = 'subsidy/tokyo23/tokyo23_housing.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'

    def get_queryset(self):
        return Subsidy.objects.filter(is_published=True, prefectures__prefecture='東京都23区', themes__theme='住まい')
