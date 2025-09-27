from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="КНИГАtime")
    site_subtitle = models.CharField(max_length=300, default="Путешествие во времени длиной в книгу")
    header_background = models.ImageField(
        upload_to='site_settings/',
        default='default_header.jpg',
        verbose_name="Фон шапки"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        # Оставляем только одну запись настроек
        if SiteSettings.objects.exists() and not self.pk:
            # Если уже есть запись, обновляем ее
            existing = SiteSettings.objects.first()
            existing.site_name = self.site_name
            existing.site_subtitle = self.site_subtitle
            existing.header_background = self.header_background
            return existing.save(*args, **kwargs)
        return super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Метод для получения единственной записи настроек
        obj, created = cls.objects.get_or_create(pk=1)
        return obj