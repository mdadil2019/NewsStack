from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from newsstack import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import topnews_view,tech_news,sports_news,science_news
urlpatterns = [
    url(r'^topnews/$',topnews_view,name='topnews_url'),
    url(r'^technews/$',tech_news,name='tech_news_url'),
    url(r'^sportsnews/$',sports_news,name='sports_news_url'),
    url(r'^sciencenews/$',science_news,name='science_news_url'),


    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
