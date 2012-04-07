from tartarus.django.conf.settings.default import *
from typhon.settings.installers import InstallersManager
import typhon
import os

ROOT_URLCONF = 'typhon.urls'

TEMPLATE_DIRS += (
    PROJECT_ROOT + '/' + 'templates',
    os.path.dirname(typhon.__file__) + '/' + 'templates',
)

INSTALLED_APPS += (
    PROJECT_NAME,
    'tartarus.django.templatetags',
    'typhon',
)

AUTOINSTALLED_APPS = InstallersManager()

TEMPLATE_CONTEXT_PROCESSORS = (
        'typhon.context_processors.static_context',
        'django.core.context_processors.request',
)

TEMPLATE_VISIBLE_SETTINGS = [ 'PROJECT_NAME' ]