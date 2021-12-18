from djongo import models as dj_models


class Environment(dj_models.Model):
    _id = dj_models.ObjectIdField()
    entities = dj_models.JSONField(default=[])
    spawn_rateo = dj_models.JSONField(default={'food': 0, 'enemy': 0})
    island = dj_models.JSONField(default={'name': 'unknown', 'border_seed': 0, 'biome_seed': 0})

    def add_entities(self, *entities):
        self.entities.extend(environment=entities)


class Simulation(dj_models.Model):
    _id = dj_models.ObjectIdField()
    environment = dj_models.EmbeddedField(model_container=Environment)
