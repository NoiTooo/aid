from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from subsidy.models import Subsidy


class SubsidySitemap(Sitemap):
    """
    subsidyのサイトマップ
    """
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Subsidy.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('subsidy:detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    """
    静的ページのサイトマップ
    """
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['subsidy:operator_information',
                'subsidy:terms_of_service',
                'subsidy:user_alert',
                'subsidy:user_alert_done',
                'subsidy:inquiry_create',
                'subsidy:inquiry_done',
                'subsidy:tokyo23_top',
                'subsidy:tokyo23_index',
                'subsidy:tokyo23_marriage',
                'subsidy:tokyo23_housing',
                ]

    def location(self, item):
        return reverse(item)
