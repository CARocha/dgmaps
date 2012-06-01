from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from settings import *
from os import path as os_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dgmaps.views.home', name='home'),
    # url(r'^dgmaps/', include('dgmaps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^$',   direct_to_template,{'template': 'index.html'}),
    (r'^$', 'lugares.views.index'),
    url(r'^lugares/', include('lugares.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
