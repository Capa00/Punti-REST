# from rest_framework import viewsets
#
# from entities.models import Entity, Punto
# from api.serializers import EntitySerializer, PuntoSerializer
#
#
# class AbsAPIView(viewsets.ModelViewSet):
#     lookup_field = 'pk'
#
#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         return self.list(request)
#
# class EntityViewSet(AbsAPIView):
#     serializer_class = EntitySerializer
#     queryset = Entity.objects.all()
#
# class PuntoViewSet(AbsAPIView):
#     serializer_class = PuntoSerializer
#     queryset = Punto.objects.all()
