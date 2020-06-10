from django.views import generic
from subsidy.models import Subsidy, City, Prefecture, Event


class Index(generic.ListView):
    template_name = 'subsidy/index.html'
    queryset = Subsidy.objects.order_by('-created_at')
    context_object_name = 'object_list'