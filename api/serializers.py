from rest_framework import serializers

from entities.models import Entity, Punto


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class SpriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        exclude = ['born_date', 'death_date']


class PuntoSerializer(serializers.ModelSerializer):
    brain = serializers.SerializerMethodField()
    dna = serializers.CharField()

    @staticmethod
    def get_brain(obj):
        try:
            brain = obj.brain
            return brain.ids
        except AttributeError:
            return

    class Meta:
        model = Punto
        fields = '__all__'
