from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',views.index),
    path('game/<slug:game_slug>/', views.game_detail, name='game-detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
