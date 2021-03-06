from __future__ import unicode_literals
from django_markdown.models import MarkdownField
from django.db import models
import datetime
from django.core.urlresolvers import reverse
from artists.models import Artist
from generic_scaffold import get_url_names

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=30)
    description = MarkdownField(blank=True)
    date = models.DateField(u"Date", default=datetime.date.today, blank=True, null=True)
    time = models.TimeField(u"Time", blank=True, null=True)
    artists = models.ManyToManyField(Artist)

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
	return reverse(get_url_names(prefix='events/')['detail'], args=(self.id, ) )

