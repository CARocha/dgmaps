from django.conf.urls import patterns, include, url
from lugares.models import Lugar

urlpatterns = patterns('lugares.views',
    url(r'^$', 'index', name='index'),
    url(r'^crear/$', 'guardar_mapa', name='guardar-mapa'),
    url(r'^ver/$', 'mostrar_globo', name='mostrar-globo'),
    url(r'^eliminar/(?P<id>\d+)/$', 'eliminar', name='eliminar'),

)