from abc import ABCMeta

class BaseInstaller(object):
    __metaclass__ = ABCMeta
    app = None
    
    def __init__(self, module):
        self.set_module(module)
        
    def set_module(self, module):
        self.module = module
    
    def install(self, config={}):
        if self.set_installed():
            self.before_install(config)
            self.set_settings(config)
            self.after_install(config)
    
    def before_install(self, config={}):
        pass
    
    def after_install(self, config={}):
        pass
    
    def set_installed(self):
        if not self.is_installed:
            self.module.INSTALLED_APPS += (self.app,)
            return True
        return False
    
    @property
    def is_installed(self):
        return self.app in self.module.INSTALLED_APPS
        
    
    def set_settings(self, config={}):
        for ban in ['app']:
            if config.has_key(ban):
                del config[ban] 
        self.__dict__.update(config)
    
    def get_urlpatterns(self):
        pass
    
