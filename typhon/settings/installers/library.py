import django
from django.conf.urls.defaults import patterns, include, url
from typhon.settings.installers.base import BaseInstaller

class DjangoContribAdminBaseInstaller(BaseInstaller):
    app = "django.contrib.admin"
    def get_urlpatterns(self):
        from django.contrib import admin
        admin.autodiscover()
        return (r'^admin/', include(admin.site.urls))
    
class UserenaInstaller(BaseInstaller):
    app = "userena"
    
    def get_settings(self):
        return dict(
            AUTHENTICATION_BACKENDS = (
                'userena.backends.UserenaAuthenticationBackend',
                'guardian.backends.ObjectPermissionBackend',
                'django.contrib.auth.backends.ModelBackend',
            ),
            ANONYMOUS_USER_ID = -1,
            LOGIN_REDIRECT_URL = '/account/%(username)s/',
            LOGIN_URL = '/account/signin/',
            LOGOUT_URL = '/account/signout/',
            INSTALLED_APPS = ('userena', 'guardian', 'easy_thumbnails'),
            AUTH_PROFILE_MODULE = '%s.UserProfile' % django.conf.settings.PROJECT_NAME,
        )
        
    def get_urlpatterns(self):
        return (r'^account/', include('userena.urls'))
    

class TyphonUsersInstaller(UserenaInstaller):
    app = "typhon.users"
        
    def get_settings(self):
        settings = super(TyphonUsersInstaller, self).get_settings()
        settings.update(
            #AUTH_PROFILE_MODULE = 'typhon.users.UserProfile',
            AUTH_PROFILE_MODULE = 'users.UserProfile',
        )
        return settings
    

class DjangoFiltersInstaller(BaseInstaller):
    app = "django_filters"