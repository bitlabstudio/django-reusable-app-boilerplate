"""URLs for appname application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('appname.views',
    url(r'^$', view='index', name='appname_index'),
)
