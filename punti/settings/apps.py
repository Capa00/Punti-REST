# Application definition

MY_APPS = [
    'scheduler',
    'entities',
    'simulations',
    'web.pcms',
]

CMS_APPS = [
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.

    'cms',  # django CMS itself
    #'mptt',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    #'south',  # Only needed for Django < 1.7
    'sekizai',  # for javascript and css management
    'treebeard',  # for javascript and css management

    # 'djangocms_file',
    # 'djangocms_flash',
    # 'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_picture',
    # 'djangocms_teaser',
    # 'djangocms_video',
    # 'djangocms_link',
    # 'djangocms_snippet',
    # 'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry
]

INSTALLED_APPS = [

    *CMS_APPS,

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    *MY_APPS,

    'rest_framework',
    'rangefilter',
    'django_json_widget',

]
