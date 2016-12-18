from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "ac5"

    def ready(self):
        import_module("ac5.receivers")
