from django.views import generic
from subsidy.models import Subsidy, City, Prefecture, Theme

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
        return Subsidy.objects.filter(prefectures__prefecture='東京都', themes__theme='結婚')