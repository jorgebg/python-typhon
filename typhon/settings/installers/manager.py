from typhon.settings.installers.base import BaseInstaller
from typhon.settings.installers import library
from tartarus.utils import get_subclasses
from django.utils import importlib
from django.conf.urls.defaults import patterns
import os
import logging

class InstallersManager(tuple):
    
    installers = {}
    
    def __init__(self, library=None):
        if not library:
            library = get_subclasses(BaseInstaller)
        self.library = library
    
    def __add__(self, other):
        for app in other:
            self.install(app)
        return InstallersManager(x + y for x, y in zip(self, other))
    
    def install(self, app, config={}):
        module = self.get_module()
        installer = self.get_installer(app)
        if not installer.is_installed:
            self.installers[app] = installer
            installer.install(config)
        elif module.DEBUG:
            logging.warning("Autoinstalled application already installed: '%s'" % app)
        return installer
    
    def get_urlpatterns(self, app=None):
        if app:
            installers = [ self.installers[app] ]
        else:
            installers = self.installers.values()
        urlpatterns = []
        for installer in installers:
            installer_urlpatterns=installer.get_urlpatterns()
            if installer_urlpatterns:
                urlpatterns += patterns('', installer_urlpatterns)
        return urlpatterns
            
    
    
    @classmethod
    def get_module(self):
        if not hasattr(self, '_module'):
            self._module = importlib.import_module(os.environ["DJANGO_SETTINGS_MODULE"])
        return self._module
    
    def get_installer(self, app):
        module = self.get_module()
        installer = None
        for i in self.library:
            if i.app == app:
                installer = i
                break
        if not installer:
            installer = self.generate_installer(app) 
        return installer(module)
    
    @classmethod
    def generate_installer(self, app):
        return type('GenericInstaller', (BaseInstaller, ), { 'app': app } )
