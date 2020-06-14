from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from subsidy.models import Subsidy, City, Prefecture, Theme
from . forms import InquiryCreateForm

"""
問い合わせ
"""
class Inquiry_create(generic.CreateView):
    """問い合わせフォーム"""
    template_name = 'subsidy/inquiry_create.html'
    form_class = InquiryCreateForm
    success_url = reverse_lazy('subsidy:inquiry_done')

class Inquiry_done(generic.TemplateView):
    """問い合わせ完了"""
    template_name = 'subsidy/inquiry_done.html'

"""
東京都23区版
"""
class Tokyo23_Top(generic.TemplateView):
    """TOPページ"""
    template_name = 'subsidy/tokyo23_top.html'

class Detail(generic.DeleteView):
    """案件詳細ページ"""
    template_name = 'subsidy/detail.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object'

class Tokyo23_marriage(generic.ListView):
    """テーマ「結婚」"""
    template_name = 'subsidy/tokyo23_marriage.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'

    def get_queryset(self):
        return Subsidy.objects.filter(prefectures__prefecture='東京都23区', themes__theme='結婚')