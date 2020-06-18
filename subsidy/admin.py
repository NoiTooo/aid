from django.contrib import admin
from .models import Inquiry, UserAlert, Subsidy, Theme


class SubsidyAdmin(admin.ModelAdmin):
    filter_horizontal = ['themes']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "themes":
            kwargs["queryset"] = Theme.objects.order_by('theme')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Subsidy, SubsidyAdmin)
admin.site.register(Theme)
admin.site.register(Inquiry)
admin.site.register(UserAlert)
