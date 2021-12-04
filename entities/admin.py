from django.contrib import admin
from django.forms import NumberInput, FloatField, ModelForm, ChoiceField, HiddenInput
from rangefilter.filters import DateRangeFilter

from punti.settings import SPRITES_TYPES
from scheduler.models import Brain
from utilities.forms import FieldsetsBuilder
from .models import Punto, Entity, Enemy, Ladder, Wall, Sprite


class SpriteAdmin(ModelForm):
    type = ChoiceField(required=True, choices=[('none', '----')]+SPRITES_TYPES, widget=HiddenInput())
    x = FloatField(required=False, widget=NumberInput(attrs={'step': "0.01"}))
    y = FloatField(required=False, widget=NumberInput(attrs={'step': "0.01"}))
    z = FloatField(required=False, widget=NumberInput(attrs={'step': "0.01"}))

    search_fields = ("type",)

    fieldsets = FieldsetsBuilder() \
        .fields('type') \
        .section('Position') \
        .fields('x', 'y', 'z') \
    .build()
    #.classes('collapse')\

    def clean(self):
        if self.Meta.model is not Entity:
            if self.cleaned_data.get('type') != self.Meta.model.__name__.lower():
                self.add_error('type', f'The type must be {self.Meta.model.__name__}.')
        return super(SpriteAdmin, self).clean()

    class Meta:
        fields = '__all__'
        model = Sprite

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    form = SpriteAdmin
    list_display = ['type', 'id', 'x', 'y', 'z', 'born_date', 'death_date']
    list_editable = ['x', 'y', 'z']

    list_filter = [
        'type',
        ('born_date', DateRangeFilter),
        ('death_date', DateRangeFilter),
    ]

    fieldsets = SpriteAdmin.fieldsets + FieldsetsBuilder() \
        .section('Life Span') \
        .fields('born_date', 'death_date') \
    .build()

    def has_add_permission(self, request, obj=None):
        return self.model.__name__.lower() != 'entity'

    def get_changeform_initial_data(self, request):
        return {
            **super(EntityAdmin, self).get_changeform_initial_data(request),
            'x': 0,
            'y': 0,
            'z': 0,
            'type': self.model.__name__.lower()

        }

    def get_changelist_form(self, request, **kwargs):
        kwargs.setdefault('form', SpriteAdmin)
        return super().get_changelist_form(request, **kwargs)

@admin.register(Punto)
class PuntoAdmin(EntityAdmin):
    list_filter = [
        ('born_date', DateRangeFilter),
        ('death_date', DateRangeFilter),
    ]

    fieldsets = EntityAdmin.fieldsets + FieldsetsBuilder() \
        .fields('brain') \
    .build()


@admin.register(Brain)
class BrainAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(previous__isnull=True)


admin.site.register(Enemy, EntityAdmin)
admin.site.register(Wall, EntityAdmin)
admin.site.register(Ladder, EntityAdmin)
