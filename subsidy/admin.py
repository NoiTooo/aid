from django.contrib import admin
from .models import Inquiry, UserAlert, Subsidy, Theme

class UserAlertAdmin(admin.ModelAdmin):
    list_display = ('response_completed', 'problem_found', 'applicable_url')
    ordering = ('updated_at',)
    list_filter = ('response_completed', 'problem_found')
    search_fields = ('response_completed', 'response_note', 'problem_found', 'applicable_url', 'other_note')



class InquiryAdmin(admin.ModelAdmin):
    list_display = ('status', 'updated_at', 'title', 'name', 'email', 'phone', 'content')
    ordering = ('updated_at',)
    list_filter = ('status', 'title', 'name', 'email')
    search_fields = ('status', 'title', 'name', 'email', 'phone', 'updated_at')


class SubsidyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'prefecture', 'city', 'official_page', 'end_at', 'updated_at')
    ordering = ('-end_at',)
    list_filter = ('is_published', 'prefecture', 'city')
    search_fields = ('name', 'prefecture', 'city')
    filter_horizontal = ['themes']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "themes":
            kwargs["queryset"] = Theme.objects.order_by('theme')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Subsidy, SubsidyAdmin)
admin.site.register(Theme)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(UserAlert, UserAlertAdmin)
