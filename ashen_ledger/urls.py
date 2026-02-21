from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importando todas as Views (AGORA COM O CAMINHO CORRETO!)
from apps.games.views import GameViewSet
from apps.bosses.views import BossViewSet
from apps.builds.views import BuildViewSet
from apps.sessions.views import PlaySessionViewSet

# O Roteador Automático
router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'bosses', BossViewSet)
router.register(r'builds', BuildViewSet)
router.register(r'sessions', PlaySessionViewSet, basename='playsession')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]