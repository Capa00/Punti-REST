class MongoRouter:
    route_app = ['simulations']

    def db_for_read(self, model, **kwargs):
        return 'mongo' if model._meta.app_label in self.route_app else None

    def db_for_write(self, model, **hints):
        return 'mongo' if model._meta.app_label in self.route_app else None

    def allow_relation(self, obj1, obj2, **hints):
        return 'mongo' if obj1._meta.app_label in self.route_app and obj2._meta.app_label in self.route_app else None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return 'mongo' if app_label in self.route_app else None
