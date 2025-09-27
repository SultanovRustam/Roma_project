import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booktime_project.settings')
django.setup()

from timeline.models import SiteSettings

def create_default_settings():
    if not SiteSettings.objects.exists():
        settings = SiteSettings(
            site_name="КНИГАtime",
            site_subtitle="Путешествие во времени длиной в книгу"
        )
        settings.save()
        print("Созданы настройки сайта по умолчанию")

if __name__ == '__main__':
    create_default_settings()