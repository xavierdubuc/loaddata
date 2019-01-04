import importlib

from django.conf import settings
from django.apps import apps
import os


class PostScriptRunner():
    # FIXME Should be a config variable
    ignored_apps = ['corsheaders', 'kronos', 'rest_framework', 'oauth2_provider', 'simple_history', 'asynchronous']
    # FIXME should be a config variable (and maybe a list of dirs ?)
    dir_name = 'post_fixture_scripts'

    @staticmethod
    def run(sender, fixtures, fixture_labels, **kwargs):
        installed_apps = settings.INSTALLED_APPS
        for app in installed_apps:
            if __class__._should_handle_app(app):
                config = apps.get_app_config(app)
                pf_scripts_path = os.path.join(config.path, __class__.dir_name)
                if os.path.exists(pf_scripts_path):
                    for file in os.listdir(pf_scripts_path):
                        chunks = file.split('.')
                        filename = '.'.join(chunks[0:-1])
                        ext = chunks[-1]
                        if ext == 'py':
                            module = importlib.import_module('.'.join([app, __class__.dir_name, filename]))
                            module.run(sender, fixtures, fixture_labels, **kwargs)
                            print('Executed', filename)

    @staticmethod
    def _should_handle_app(app):
        return not app.startswith('django') and not app.startswith('oa') and app not in __class__.ignored_apps
