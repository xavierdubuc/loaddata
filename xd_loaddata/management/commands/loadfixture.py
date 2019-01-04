from django.core.management.commands.loaddata import Command as BaseCommand
from xd_loaddata.signals import post_loaddata

class Command(BaseCommand):
    help = BaseCommand.help + ' (surcharged to send a signal when load is finished)'
    def handle(self, *fixture_labels, **options):
        super().handle(*fixture_labels, **options)
        fixtures = [item for sublist in [self.find_fixtures(fixture_label) for fixture_label in fixture_labels] for item in sublist]
        post_loaddata.send(sender=self.__class__, fixtures=fixtures, fixture_labels=fixture_labels)
