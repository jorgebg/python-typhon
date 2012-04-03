from django.template.loaders.app_directories import Loader, app_template_dirs
from typhon.views import ModelResource
import os

class Loader(Loader):
    is_usable = True
    def get_template_sources(self, template_name, template_dirs=None):
        if not template_dirs:
            template_dirs = app_template_dirs
        model_template_dirs = [ os.path.join(dir, ModelResource.current_template_path) for dir in template_dirs ]
        template_dirs = tuple(model_template_dirs) + template_dirs
        return super(Loader, self).get_template_sources(template_name, template_dirs)



#===============================================================================
# import os
# import re
# from django.conf import settings
# from django.template.loader import BaseLoader, TemplateDoesNotExist
# import typhon
# 
# class Loader(BaseLoader):
#    is_usable = True
# 
#    def load_template_source(self, template_name, template_dirs=None):
#        basepath = os.path.dirname(typhon.__file__)+'/templates/'
#        filepath = basepath+template_name
#        if not os.path.isfile(filepath):
#            names = ['confirm_delete', 'detail', 'form', 'list']
#            for name in names:
#                if re.match(r'.*_%s\.html' % name, template_name):
#                    file = 'model_%s.html' % name
#                    break
#            filepath = basepath+file
#        if filepath:
#            try:
#                file = open(filepath)
#                try:
#                    return (file.read().decode(settings.FILE_CHARSET), filepath)
#                finally:
#                    file.close()
#            except IOError:
#                pass
#        raise TemplateDoesNotExist(template_name)
#===============================================================================