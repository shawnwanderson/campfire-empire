from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from artists import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.artist, name="artist"),
]

