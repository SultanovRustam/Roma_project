from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'updated_at']

    def has_add_permission(self, request):
        # Запрещаем создавать новые записи, только одна запись настроек
        return not SiteSettings.objects.exists()