from django.conf.urls.defaults import *

urlpatterns = patterns('apps.tools.views',
    (r'^parseURL/$', 'parseURL'),
)
