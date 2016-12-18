from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from artists import urls
from accounts import views

urlpatterns = [
    url(r"^signup/", views.signup, name="signup"),
    url(r"^$", include("account.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
