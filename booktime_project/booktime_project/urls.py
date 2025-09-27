from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from eras.views import about  # импортируем view about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timeline.urls')),
    path('about/', about, name='about'),  # переносим about на верхний уровень
    path('eras/', include('eras.urls')),  # оставляем только era_detail
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)