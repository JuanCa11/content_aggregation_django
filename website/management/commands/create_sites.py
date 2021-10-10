from django.core.management.base import BaseCommand, CommandError
from website.models import Site
from feedparser import parse

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        Site.objects.get_or_create(name='techcrunch', rss_link='https://techcrunch.com/feed/')
        Site.objects.get_or_create(name='mashable', rss_link='https://mashable.com/feeds/rss/all')
        Site.objects.get_or_create(name='the verge', rss_link='https://www.theverge.com/rss/index.xml')