from typhon.views import autodiscover
from django.conf import settings

urlpatterns = []
urlpatterns += autodiscover()
if (hasattr(settings, 'AUTOINSTALLED_APPS')):
    urlpatterns += settings.AUTOINSTALLED_APPS.get_urlpatterns()