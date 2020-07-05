from datetime import datetime
from datetime import date
from functools import reduce
from operator import and_

from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from .models import Subsidy
from .forms import InquiryCreateForm, UserAlertForm


"""
共通情報
"""

class About_Service(generic.TemplateView):
    """サービス情報"""
    template_name = 'subsidy/common_information/about_service.html'


class Webmaster(generic.TemplateView):
    """運営者情報"""
    template_name = 'subsidy/common_information/webmaster.html'


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


class Tokyo23_Top(generic.ListView):
    """TOPページ"""
    template_name = 'subsidy/tokyo23/tokyo23_top.html'
    queryset = Subsidy.objects.order_by('-created_at')[0:5]
    context_object_name = 'object_list'


class Detail(generic.DeleteView):
    """案件詳細ページ"""
    template_name = 'subsidy/common_information/detail.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object'

class Tokyo23_Index(generic.ListView):
    """23区でフリーワード検索、全案件一覧"""
    template_name = 'subsidy/tokyo23/tokyo23_index.html'
    model = Subsidy
    paginate_by = 5

    def get_queryset(self):
        today = date.today()
        queryset = Subsidy.objects.order_by('-updated_at').filter(prefecture=1).distinct()
        #filter(end_at__gte=today)
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i
            query = reduce(
                        and_, [Q(name__icontains=q) |
                               Q(prefecture__icontains=q)|
                               Q(city__icontains=q)|
                               Q(support_amount_note__icontains=q) |
                               Q(description__icontains=q) |
                               Q(condition__icontains=q)|
                               Q(referrer__icontains=q) |
                               Q(themes__theme__icontains=q)
                               for q in q_list]
                    )
            queryset = queryset.filter(query)
        return queryset

    #「」検索結果:「」件の取得
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword', '')
        keyword = self.request.GET.get('keyword', '')
        ctx['count'] = Subsidy.objects.filter(
            Q(name__icontains=keyword) |
            Q(prefecture__icontains=keyword)|
            Q(city__icontains=keyword)|
            Q(support_amount_note__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(condition__icontains=keyword)|
            Q(referrer__icontains=keyword) |
            Q(themes__theme__icontains=keyword)).count()
        return ctx


class Tokyo23_Category_Select(generic.ListView):

    """    23区で「エリア(市区町村)」と「テーマ」でAND検索する """

    template_name = 'subsidy/tokyo23/tokyo23_index.html'
    model = Subsidy
    paginate_by = 5


    def get_queryset(self):
        today = date.today()
        city = self.request.GET.get('city')
        theme = self.request.GET.get('theme')
        queryset = Subsidy.objects.filter(prefecture=1, city=city, themes__theme=theme).order_by('-updated_at').distinct()
        #filter(end_at__gte=today)
        """ city か theme どちらか、あるいはどちらも空の場合の処理 """
        if city=="" and theme=="":
            queryset = Subsidy.objects.filter(prefecture=1).order_by('-updated_at').distinct()
        elif city=="":
            queryset = Subsidy.objects.filter(themes__theme=theme, prefecture=1).distinct()
        elif theme=="":
            queryset = Subsidy.objects.filter(city=city, prefecture=1).order_by('-updated_at').distinct()
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        theme = self.request.GET.get('theme')
        if city=="" and theme=="":
            ctx['count'] = Subsidy.objects.all().order_by('-updated_at').count()
        elif city=="":
            ctx['count'] = Subsidy.objects.filter(themes__theme=theme, prefecture=1).distinct().count()
        elif theme=="":
            ctx['count'] = Subsidy.objects.filter(city=city, prefecture=1).order_by('-updated_at').distinct().count()
        else:
            ctx['count'] = Subsidy.objects.filter(prefecture=1, city=city, themes__theme=theme).order_by('-updated_at').count()
        return ctx

class Childbirth_Childcare(generic.ListView):
    """テーマ「出産・子供」一覧"""
    template_name = 'subsidy/tokyo23/childbirth_childcare.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'
    paginate_by = 5


    def get_queryset(self):
        today = date.today()
        return Subsidy.objects.filter(is_published=True, prefecture=1, themes__theme='出産・子供').order_by('-updated_at').distinct()
        #filter(end_at__gte=today)


class Ceremonial_Occasion(generic.ListView):
    """テーマ「冠婚葬祭」一覧"""
    template_name = 'subsidy/tokyo23/ceremonial_occasion.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'
    paginate_by = 5


    def get_queryset(self):
        today = date.today()
        return Subsidy.objects.filter(is_published=True, prefecture=1, themes__theme='冠婚葬祭').order_by('-updated_at').distinct()
        #filter(end_at__gte=today)


class Housing(generic.ListView):
    """テーマ「住まい」一覧"""
    template_name = 'subsidy/tokyo23/housing.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        today = date.today()
        return Subsidy.objects.filter(is_published=True, prefecture=1, themes__theme='住まい').order_by('-updated_at').distinct()
        #filter(end_at__gte=today)


class Others(generic.ListView):
    """テーマ「その他」一覧"""
    template_name = 'subsidy/tokyo23/others.html'
    queryset = Subsidy.objects.all()
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        today = date.today()
        return Subsidy.objects.filter(is_published=True, prefecture=1, themes__theme='その他').order_by('-updated_at').distinct()
        #filter(end_at__gte=today)