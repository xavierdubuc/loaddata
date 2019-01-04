Permissions
=====

Quick start
-----------

Add "xd_loaddata" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = [
    ...
    'xd_loaddata',
]
```

Signal
-----------

If you use `loadfixture` command instead of default `loaddata`, a signal is emitted at the end of the process.
You can use the signal `post_loaddata` to execute some piece of code after the command has been executed.

The signal comes with two params :

- `fixtures` which contains all the executed fixtures,
- `fixture_labels` which contains all the labels given to the command


Example ::

```python
from django.dispatch import receiver
from xd_loaddata.signals import post_loaddata
@receiver(post_loaddata)
def post_loaddata_handling(sender, fixtures, fixture_labels, **kwargs):
    # your code here
```

Don't forget to load your signals in the `apps.py` like this ::

```python
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from . import signals
```

You'll probably also need to define your app config in the init file of your module ::

```python
# myapp/__init__.py

default_app_config = 'myapp.apps.MyAppConfig'
```
