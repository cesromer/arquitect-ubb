from django.conf.urls.defaults import *
from piston.resource import Resource
#from piston.authentication import HttpBasicAuthentication
from api.handlers import BlogPostHandler, ArbitraryDataHandler

#auth = HttpBasicAuthentication(realm="My Realm")
#ad = { 'authentication': auth }

blogpost_resource = Resource(handler=BlogPostHandler)#, **ad)
arbitrary_resource = Resource(handler=ArbitraryDataHandler)#, **ad)

urlpatterns = patterns('',
    url(r'^imagenes/(?P<post_slug>[^/]+)/$', blogpost_resource),
    url(r'^other/(?P<username>[^/]+)/(?P<data>.+)/$', arbitrary_resource),
    url(r'^$', 'api.views.home'),
)
