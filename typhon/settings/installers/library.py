import django
from django.conf.urls.defaults import patterns, include, url
from typhon.settings.installers.base import BaseInstaller     

class DjangoContribAdminBaseInstaller(BaseInstaller):
    app = "django.contrib.admin"
    def get_urlpatterns(self):
        from django.contrib import admin
        admin.autodiscover()
        return (r'^admin/', include(admin.site.urls))
    
class UserenaBaseInstaller(BaseInstaller):
    app = "userena"
    
    def set_urlpatterns(self, urlpatterns):
        return (r'^accounts/', include('userena.urls'))
    

class DjangoFiltersInstaller(BaseInstaller):
    app = "django_filters"