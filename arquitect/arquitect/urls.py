from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arquitect.views.home', name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^$', 'homepage.views.home', name='Pagina Inicial'),
    url(r'^imagenes/(?P<slug>[-\w]+)$', include('homepage.urls')),
    url(r'^tags/(?P<tagg>[- \w]+)$', 'homepage.views.tagged'),
    url(r'^documentos/(?P<slug>[-\w]+)$', 'homepage.views.single_doc'),
    url(r'^tags/$', 'homepage.views.all_tags'),
    url(r'^documentos/$', 'homepage.views.all_docs'),
    url(r'^contacto/$', 'homepage.views.contact', name='Contacto'),
    url(r'^busqueda/$', 'homepage.views.search', name="Busqueda"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    (r'^login/$', 'django.contrib.auth.views.login',
                {'template_name': 'homepage/index.html', }),
    (r'^logout/$', 'homepage.views.logout_view', ),

)
