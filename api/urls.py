from rest_framework import routers
from django.urls import path, include

from api.views import EntityViewSet, PuntoViewSet, WallViewSet, LadderViewSet, EnemyViewSet, SpriteViewSet
from punti.settings import api_version

router = routers.DefaultRouter()
router.register('sprites', SpriteViewSet)
router.register('entities', EntityViewSet)
router.register('punti', PuntoViewSet)
router.register('walls', WallViewSet)
router.register('ladders', LadderViewSet)
router.register('enemies', EnemyViewSet)

urlpatterns = [
    path(f'v{api_version}/', include(router.urls)),
]
