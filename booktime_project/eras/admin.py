from django.contrib import admin
from .models import Era, EraPage, EraImage

class EraImageInline(admin.TabularInline):
    model = EraPage.images.through
    extra = 1

class EraPageAdmin(admin.ModelAdmin):
    inlines = [EraImageInline]
    exclude = ('images',)

admin.site.register(Era)
admin.site.register(EraPage, EraPageAdmin)
admin.site.register(EraImage)