from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

from django.contrib.auth.models import User

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name
        
    def get_absolute_url(self):
	return reverse(get_url_names(prefix='artists')['detail'], args=(self.id, ) )


@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_artist(sender, instance, **kwargs):
    instance.artist.save()
