from django.conf.urls.defaults import *

urlpatterns = patterns('apps.links.views',
    (r'^$', 'main'),
    (r'^g/(?P<slug>[\w_-]+)/$', 'group')
)
