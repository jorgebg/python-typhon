from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

def static_context(request):
    """
    Adds the settings specified in context module to
    the request context.
    """
    if not hasattr(static_context,'data'):
            from django.conf import settings
            context = import_module('%s.context'%settings.PROJECT_NAME)   
            data = {}
            for attr in dir(context):
                data[attr] = getattr(context, attr)
            static_context.data = data
    return static_context.data