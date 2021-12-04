from django.core.exceptions import FieldError
from rest_framework import viewsets

from api.exceptions import FieldDoesNotExist
from api.serializers import EntitySerializer, PuntoSerializer, SpriteSerializer
from entities.models import Punto, Wall, Ladder, Enemy, Entity


class AbsAPIView(viewsets.ModelViewSet):
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        query_params = request.GET.dict()
        try:
            self.queryset = self.queryset.filter(**query_params)
        except FieldError:
            fields = [next(f for f in query_params.keys() if f.split('__')[0] not in self.queryset.model._meta.fields)]
            raise FieldDoesNotExist(self, fields)

        return super().list(request, *args, **kwargs)


class EntityViewSet(AbsAPIView):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()


class SpriteViewSet(EntityViewSet):
    serializer_class = SpriteSerializer


class PuntoViewSet(AbsAPIView):
    serializer_class = PuntoSerializer
    queryset = Punto.objects.all()


class WallViewSet(AbsAPIView):
    serializer_class = EntitySerializer
    queryset = Wall.objects.all()


class LadderViewSet(AbsAPIView):
    serializer_class = EntitySerializer
    queryset = Ladder.objects.all()


class EnemyViewSet(AbsAPIView):
    serializer_class = EntitySerializer
    queryset = Enemy.objects.all()
