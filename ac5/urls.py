from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from artists import urls as artists_urls
from accounts import urls as accounts_urls
from account import views as account_views
import ac5.account_views

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^artists/", include(artists_urls)),
    url(r"^admin/", include(admin.site.urls)),
    #url(r"^account/", include(accounts_urls)),
    #url(r"^account/", include("account.urls")),
    url(r'^avatar/', include('avatar.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
]

urlpatterns += [
    url(r"^account/signup/$", ac5.account_views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from art.scaffolding import ArtCrudManager
art_crud = ArtCrudManager()
urlpatterns += art_crud.get_url_patterns()

from events.scaffolding import EventCrudManager
event_crud = EventCrudManager()
urlpatterns += event_crud.get_url_patterns()
