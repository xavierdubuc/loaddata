from django.apps import AppConfig


class XdLoadDataConfig(AppConfig):
    name = 'xd_loaddata'

    def ready(self):
        from . import signals
