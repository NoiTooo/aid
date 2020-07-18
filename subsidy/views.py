from datetime import datetime
from datetime import date
from encodings import cp932
from functools import reduce
from operator import and_

from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Subsidy
from .forms import InquiryCreateForm, UserAlertForm

import csv
import io
from django.http import HttpResponse
from .forms import CSVUploadForm


"""
共通情報
"""


class About_Service(generic.TemplateView):
    """サービス情報"""
    template_name = 'subsidy/common_information/about_service.html'


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


class PostIndex(generic.ListView):
    template_name = 'subsidy/csv/post_list.html'
    model = Subsidy


class PostImport(generic.FormView):
    template_name = 'subsidy/csv/import.html'
    success_url = reverse_lazy('subsidy:index')
    form_class = CSVUploadForm

    def form_valid(self, form):
        form.save()
        return redirect('subsidy:db_index')


def post_export(request):
    response = HttpResponse(content_type='text/csv', charset='cp932')
    response['Content-Disposition'] = 'attachment; filename="posts.csv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response)
    for post in Subsidy.objects.all():
        writer.writerow([post.pk, post.name, post.prefecture, post.city, post.target, post.condition, post.overview, post.description, post.maximum_support_amount, post.support_amount_note, post.how_to_apply, post.start_at, post.end_at, post.referrer, post.official_page, post.is_published, post.created_at, post.updated_at, post.themes])
    return response

"""
東京都23区版
"""
tokyo = '東京都' or '全国'


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
    queryset = Subsidy.objects.filter(is_published=True)
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        today = date.today()
        queryset = Subsidy.objects.order_by('-updated_at').filter(is_published=True, prefecture=tokyo).distinct()
        # filter(end_at__gte=today)
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
                       Q(prefecture__icontains=q) |
                       Q(city__icontains=q) |
                       Q(support_amount_note__icontains=q) |
                       Q(description__icontains=q) |
                       Q(condition__icontains=q) |
                       Q(referrer__icontains=q) |
                       Q(themes__theme__icontains=q)
                       for q in q_list]
            )
            queryset = queryset.filter(query, is_published=True, prefecture=tokyo)
        return queryset

    # 「」検索結果:「」件の取得
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('keyword', '')
        ctx['keyword'] = self.request.GET.get('keyword', '')
        keyword = self.request.GET.get('keyword', '')

        count = Subsidy.objects.filter(
            Q(name__icontains=keyword) |
            Q(prefecture__icontains=keyword) |
            Q(city__icontains=keyword) |
            Q(support_amount_note__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(condition__icontains=keyword) |
            Q(referrer__icontains=keyword) |
            Q(themes__theme__icontains=keyword)).count()
        ctx['count'] = Subsidy.objects.filter(
            Q(name__icontains=keyword) |
            Q(prefecture__icontains=keyword) |
            Q(city__icontains=keyword) |
            Q(support_amount_note__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(condition__icontains=keyword) |
            Q(referrer__icontains=keyword) |
            Q(themes__theme__icontains=keyword)).count()
        # for Pagination
        page = self.request.GET.get('page')
        ctx['page'] = page
        if page is None or int(page) == 1:
            ctx['pagecountstart'] = 1
            ctx['pagecountend'] = count
        else:
            ctx['pagecountstart'] = int(page) * 10 - 9
            ctx['pagecountend'] = int(page) * 10
        return ctx


class Tokyo23_Category_Select(generic.ListView):
    """    23区で「エリア(市区町村)」と「テーマ」でAND検索する """

    template_name = 'subsidy/tokyo23/tokyo23_index.html'
    queryset = Subsidy.objects.filter(is_published=True).order_by('-update_at')
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        today = date.today()
        city = self.request.GET.get('city')
        theme = self.request.GET.get('theme')
        queryset = Subsidy.objects.filter(is_published=True, prefecture=tokyo, city=city, themes__theme=theme).order_by(
            '-updated_at').distinct()
        # filter(end_at__gte=today)
        """ city か theme どちらか、あるいはどちらも空の場合の処理 """
        if city == "" and theme == "":
            queryset = Subsidy.objects.filter(is_published=True, prefecture=tokyo).order_by('-updated_at').distinct()
        elif city == "":
            queryset = Subsidy.objects.filter(is_published=True, themes__theme=theme, prefecture=tokyo).order_by(
                '-updated_at').distinct()
        elif theme == "":
            queryset = Subsidy.objects.filter(is_published=True, city=city, prefecture=tokyo).order_by(
                '-updated_at').distinct()
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        city = self.request.GET.get('city')
        theme = self.request.GET.get('theme')
        ctx['query'] = '地域：' + city + '　' + 'テーマ：' + theme
        ctx['city'] = city
        ctx['theme'] = theme
        if city == "" and theme == "":
            count = Subsidy.objects.all().filter(is_published=True).order_by('-updated_at').distinct().count()
            ctx['count'] = Subsidy.objects.all().filter(is_published=True).order_by('-updated_at').distinct().count()
        elif city == "":
            count = Subsidy.objects.filter(is_published=True, themes__theme=theme, prefecture=tokyo).order_by(
                '-updated_at').distinct().count()
            ctx['count'] = Subsidy.objects.filter(is_published=True, themes__theme=theme, prefecture=tokyo).order_by(
                '-updated_at').distinct().count()
        elif theme == "":
            count = Subsidy.objects.filter(is_published=True, city=city, prefecture=tokyo).order_by(
                '-updated_at').distinct().count()
            ctx['count'] = Subsidy.objects.filter(is_published=True, city=city, prefecture=tokyo).order_by(
                '-updated_at').distinct().count()
        else:
            count = Subsidy.objects.filter(is_published=True, prefecture=tokyo, city=city,
                                           themes__theme=theme).order_by('-updated_at').count()
            ctx['count'] = Subsidy.objects.filter(is_published=True, prefecture=tokyo, city=city,
                                                  themes__theme=theme).order_by('-updated_at').count()
        # for Pagination
        page = self.request.GET.get('page')
        ctx['page'] = page
        if page is None or int(page) == 1:
            ctx['pagecountstart'] = 1
            ctx['pagecountend'] = count
        else:
            ctx['pagecountstart'] = int(page) * 10 - 9
            ctx['pagecountend'] = int(page) * 10
        return ctx