from __future__ import unicode_literals
from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from artists.models import Artist
from generic_scaffold import get_url_names
# Create your models here.

class Art(models.Model):
    title = models.CharField(max_length=30)
    description = MarkdownField(blank=True)
    artists = models.ManyToManyField(Artist)

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
	return reverse(get_url_names(prefix='art/')['detail'], args=(self.id, ) )


