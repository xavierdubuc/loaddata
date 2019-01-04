import django.dispatch
from django.dispatch import receiver
from xd_loaddata.post_script_runner import PostScriptRunner

post_loaddata = django.dispatch.Signal(providing_args=['fixtures', 'fixture_labels'])


@receiver(post_loaddata)
def post_loaddata_handling(sender, fixtures, fixture_labels, **kwargs):
    # FIXME Make the activation of this configurable
    PostScriptRunner.run(sender, fixtures, fixture_labels, **kwargs)
