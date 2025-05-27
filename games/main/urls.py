from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',views.index),
    path('Action/',views.get_action),
    path('Race/',views.get_race),
    path('Finance/',views.get_finance),
    path('Strategy/',views.get_strategy),
    path('game/<slug:game_slug>/', views.game_detail, name='game-detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
