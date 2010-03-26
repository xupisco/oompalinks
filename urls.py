from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin

import os, sys
ROOT_PATH = os.path.dirname(__file__)

admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(ROOT_PATH, 'media/admin')}),

    # Static serve (local)
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(ROOT_PATH, 'static')}),

    # Show apps...
    (r'^tools/', include('apps.tools.urls')),
    (r'^', include('apps.links.urls')),
)
