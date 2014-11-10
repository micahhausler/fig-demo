import logging

from bs4 import BeautifulSoup
import requests

from .models import Page
from fig_demo.celery import FigDemoTask

LOG = logging.getLogger(__name__)


class PageFetchTask(FigDemoTask):
    """
    Do stuff
    """
    def run(self, page_id):
        page = Page.objects.get(id=page_id)

        response = requests.get(page.url)

        page.record_call(response.text, response.status_code)


class CreateRecordsTask(FigDemoTask):
    """
    Create pages
    """
    def run(self, source_page=None):

        source_page = source_page or 'http://noogastartups.com'

        soup = BeautifulSoup(requests.get(source_page).text)

        domains = set()

        for anchor in soup.find_all('a'):
            if anchor['href'].startswith('http'):
                domains.add(anchor['href'])
                LOG.info('Added domain {}'.format(anchor['href']))

        Page.objects.bulk_create(
            [Page(url=url) for url in domains]
        )
