from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.era_detail, name='era_detail'),
]