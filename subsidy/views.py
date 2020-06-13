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
    model = Subsidy
    def get_queryset(self):
        return Subsidy.objects.filter(themes__theme='結婚')
