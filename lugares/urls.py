from django.conf.urls import patterns, include, url
from lugares.models import Lugar

urlpatterns = patterns('lugares.views',
    #url(r'^$', 'index', name='index'),
    url(r'^crear/$', 'guardar_mapa', name='guardar-mapa'),


)