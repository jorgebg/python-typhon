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
    'typhon',
)

AUTOINSTALLED_APPS = InstallersManager()