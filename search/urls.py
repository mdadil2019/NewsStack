from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from newsstack import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import search_view
urlpatterns = [
    url(r'^search/$',search_view,name='query_url'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
