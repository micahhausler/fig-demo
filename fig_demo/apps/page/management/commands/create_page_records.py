from django.core.management.base import BaseCommand

from fig_demo.apps.page.tasks import CreateRecordsTask


class Command(BaseCommand):
    help = """Kick off the CreateRecordsTask"""

    def handle(self, *args, **options):

        t = CreateRecordsTask()
        t.delay()
