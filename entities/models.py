from django.db import models
from django.db.models import SET_NULL

from punti.settings import SPRITES_TYPES
from scheduler.models import Brain

class Sprite(models.Model):
    type = models.CharField(max_length=255, choices=SPRITES_TYPES)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    z = models.FloatField(default=0)

    class Meta:
        abstract = True


class Entity(Sprite):
    born_date = models.DateTimeField(blank=True, null=True)
    death_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'[{str(self.id)}] {self.type.capitalize()} ({"x=%.2f" % self.x}, {"y=%.2f" % self.y}, {"z=%.2f" % self.z})'

    class Meta:
        verbose_name_plural = 'Entities'


class Punto(Entity):
    brain = models.ForeignKey(Brain, null=True, on_delete=SET_NULL, blank=True)

    @property
    def dna(self):
        if self.brain:
            return self.brain.dna

    class Meta:
        verbose_name_plural = 'Punti'


class Enemy(Entity):
    class Meta:
        verbose_name_plural = 'Enemies'


class Ladder(Entity): pass


class Wall(Entity): pass
