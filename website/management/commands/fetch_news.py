from django.core.management.base import BaseCommand, CommandError
from website.models import Site, New
from feedparser import parse
from datetime import datetime


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        for site in Site.objects.all():
            feed_url = site.rss_link
            news_feed = parse(feed_url)
            for new in news_feed.entries:
                try:
                    author = None if 'author' not in new else new.author
                    if site.name == 'mashable':
                        pub_date = datetime.strptime(new.published,
                                                     '%a, %d %b %y %H:%M:%S +0000')
                    elif site.name == 'techcrunch':
                        pub_date = datetime.strptime(new.published,
                                                     '%a, %d %b %Y %H:%M:%S +0000')
                    else:
                        pub_date = datetime.strptime(new.published,
                                                     '%Y-%m-%dT%H:%M:%S-04:00')

                    New.objects.get_or_create(site=site,
                                              title=new.title,
                                              summary=new.summary,
                                              author=author,
                                              link=new.link,
                                              pub_date=pub_date)
                except New.IntegrityError:
                    raise CommandError('New "%s" exists for site "%s" ' % new.title, site.name)
