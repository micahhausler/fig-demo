from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """
    Account Admin
    """
    list_display = ['user', 'uuid']
    search_fields = ['user', 'uuid', 'metadata']
