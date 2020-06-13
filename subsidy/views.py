from django.views import generic
from subsidy.models import Subsidy, City, Prefecture, Theme

"""
東京都23区版
"""
class Tokyo23_Top(generic.TemplateView):
    """TOPページ"""
    template_name = 'subsidy/tokyo23_top.html'

class Tokyo23_Marriage(generic.ListView):
    """テーマ「結婚」"""
    template_name = 'subsidy/tokyo23_marriage.html'
    queryset = Subsidy.objects.filter(themes=1, prefectures=2).order_by('-end_at')
    context_object_name = 'object_list'
