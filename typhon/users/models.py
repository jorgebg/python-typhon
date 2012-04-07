from userena.models import UserenaLanguageBaseProfile, PROFILE_PERMISSIONS
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class AbstractUserProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    class Meta:
        abstract = True
        permissions = PROFILE_PERMISSIONS

class UserProfile(AbstractUserProfile):
    pass
