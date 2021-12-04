# set my ordering list
from django.contrib import admin
from django.utils.translation import gettext_lazy

admin.AdminSite.site_header = gettext_lazy(
    ' _ _ _̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡| ̲▫̲͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡._ _ _'
    '٩(   ͡๏  ̯͡๏)۶_( PUNTI )_ᕕ( ᐛ )ᕗ'
    ' _ _ _̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡| ̲▫̲͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡._ _ _'
    
    ' _ _ ┻━┻︵  \(°□°)/ ︵ ┻━┻ '
)
admin.AdminSite.index_title = gettext_lazy(
    '┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓'
    "  BACK TO 90's  "
    '┏(-_-)┛┗(-_-﻿ )┓┗(-_-)┛┏(-_-)┓'
)

from punti.settings.api import api_version

CUSTOM_ADMIN_APPS = [
    {
        'name': f'api v{api_version}',
        'app_label': 'api',
        'app_url': f'/api/v{api_version}',
        'models': [
            {
                'name': name,
                'admin_url': f'/api/v{api_version}/{name.lower()}/',
                'add_url': f'/api/v{api_version}/{name.lower()}/0/',
                'view_only': True

            } if name else {'name': ''}

            for name, obj_name in [
                ('', ''), ('Sprites', 'Sprite'),
                ('', ''), ('Entities', 'Entity'),
                ('', ''), ('Punti', 'Punto'),
                ('', ''), ('Walls', 'Wall'),
                ('', ''), ('Ladders', 'Ladder'),
                ('', ''), ('Enemies', 'Enemy')
            ]
        ]
    },
]

ADMIN_ORDERING = {
    'update_apps': {'entities': {'app_url': '/admin/entities/entity'}},

    'custom_apps': CUSTOM_ADMIN_APPS,
    'apps_order': ['auth', '', 'entities', 'scheduler', '', 'api v1', ''],

    'exclude_apps': [],

    'exclude_models': {'entities': ['Entities']},

    'models_order': {'entities': ['', 'Punti', *['' for i in range(1*2 + 1)]]},

    'update_models': {
        #'entities': {'Entities': {'view_only': True}}
    },
}

# Creating a sort function
def get_app_list(self, request):
    app_dict = self._build_app_dict(request)

    if not app_dict:
        return []

    for app, models in ADMIN_ORDERING['update_models'].items():
        for model, updated_model in models.items():
            model = next(x for x in app_dict[app]['models'] if x['name'] == model)
            model.update(updated_model)

    for app, updated_app in ADMIN_ORDERING['update_apps'].items():
        app_dict[app].update(updated_app)

    for custom_app in ADMIN_ORDERING['custom_apps']:
        app_dict[custom_app['name']] = custom_app

    for app, models in ADMIN_ORDERING['exclude_models'].items():
        for model in models:
            app_dict[app]['models'].remove(next(x for x in app_dict[app]['models'] if x['name'] == model))

    for app, models_list in ADMIN_ORDERING['models_order'].items():
        app = app_dict[app]
        app_models = app['models']
        models = []
        for model_name in models_list:
            try:
                if isinstance(model_name, (tuple, list)):
                    model = next(x for x in app['models'] if x['name'] == model_name[0])
                    model['name'] = model_name[1]
                else:
                    model = next(x for x in app['models'] if x['name'] == model_name)
            except StopIteration:
                model = ''
                app_models.append(model)

            models.append(app_models.pop(app_models.index(model)))

        models.extend(app_models)
        app['models'] = models

    for app in ADMIN_ORDERING['exclude_apps']:
        app_dict.pop(app)

    app_list = []
    for app in ADMIN_ORDERING['apps_order']:

        rename = None
        if isinstance(app, (tuple, list)):
            app, rename = app[0], app[1]

        if app in app_dict:
            if rename:
                app_dict[app]['name'] = rename
            app_list.append(app_dict.pop(app))
        elif app == '':
            app_list.append({'name': '', 'models': [{'name': ''}]},)

    app_list.extend([x for _, x in app_dict.items()])

    return app_list


# Covering django.contrib.admin.AdminSite.get_app_list
admin.AdminSite.get_app_list = get_app_list
