from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    rss_link = models.CharField(max_length=200)
    click_tracking = models.IntegerField(default=0)


class New(models.Model):
    title = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    summary = models.CharField(max_length=4000)
    author = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    class Meta:
        unique_together = ('title', 'site')
