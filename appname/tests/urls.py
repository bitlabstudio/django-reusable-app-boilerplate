from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^example/', include('appname.urls')),
)
