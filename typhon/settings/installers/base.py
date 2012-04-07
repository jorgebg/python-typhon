from abc import ABCMeta

class BaseInstaller(object):
    __metaclass__ = ABCMeta
    app = None
    
    def __init__(self, module):
        self.set_module(module)
        
    def set_module(self, module):
        self.module = module
    
    def install(self, config={}):
        if not self.is_installed:
            self.set_config(config)
            self.before_install()
            self.set_settings()
            self.after_install()
            self.set_installed()
    
    def set_installed(self):
        if not self.is_installed:
            self.module.INSTALLED_APPS += (self.app,)
            return True
        return False
    
    @property
    def is_installed(self):
        return self.app in self.module.INSTALLED_APPS
        
    
    def set_config(self, config={}):
        for ban in ['app']:
            if config.has_key(ban):
                del config[ban] 
        self.__dict__.update(config)
    
    def set_settings(self, settings=None):
        if not settings:
            settings = self.get_settings()
        if settings:
            for key,default in settings.iteritems():
                value = getattr(self.module, key, None)
                if not hasattr(self.module, key):
                    value = default
                elif isinstance(value, tuple) or isinstance(value, list):
                    for dv in default:
                        if dv not in value:
                            value += (dv,)
                setattr(self.module, key, value)
                
                
    
    def get_settings(self):
        pass   
    
    def get_urlpatterns(self):
        pass
    

    
    def before_install(self):
        pass
    
    def after_install(self):
        pass