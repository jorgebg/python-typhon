from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Shows the settings'

    def handle(self, *args, **options):
        for setting in dir(settings):
            print '%s: %s' % (setting, getattr(settings, setting))