from django.contrib import admin
from .models import Subsidy, City, Prefecture, Event


class SubsidyAdmin(admin.ModelAdmin):
    filter_horizontal = ['prefectures', 'cities', 'events']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "prefectures":
            kwargs["queryset"] = Prefecture.objects.order_by('prefecture')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Subsidy, SubsidyAdmin)
admin.site.register(City)
admin.site.register(Prefecture)
admin.site.register(Event)