from django.conf.urls import url, patterns, include
from django.conf import settings

urlpatterns = patterns('content.views',
    (r'^$', 'site'),
    (r'^autocomplete$', 'autocomplete'),
    (r'^search$', 'search'),
    (r'^(?P<page_id>\d+)$', 'page'),
    (r'^(?P<page_id>\d+)/edit$', 'page_edit'),
)
