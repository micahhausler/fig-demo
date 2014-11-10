from django.contrib import admin
from django.contrib import messages

from .models import Page
from .tasks import PageFetchTask


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Page Admin
    """
    list_display = ['url', 'status_code', 'called_time']
    search_fields = ['url', 'response', 'called_time']

    actions = ['fetch', 'clear']

    def clear(self, request, queryset):
        n = queryset.count()
        if n:
            for page in queryset.all():
                page.clear_call()
            self.message_user(
                request,
                'Successfully cleared {n} pages'.format(n=n),
                messages.constants.SUCCESS
            )
    clear.short_description = 'Clear the selected %(verbose_name_plural)s'

    def fetch(self, request, queryset):
        n = queryset.count()
        if n:
            for page_id in queryset.values_list('id', flat=True):
                task = PageFetchTask()
                task.delay(page_id=page_id)
            self.message_user(
                request,
                'Successfully triggered {n} page tasks.'.format(n=n),
                messages.constants.SUCCESS
            )

    fetch.short_description = 'Start fetching selected %(verbose_name_plural)s'
