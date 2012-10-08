from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arquitect.views.home', name='home'),
    url(r'^$', 'homepage.views.home', name='Pagina Inicial'),
    url(r'^contacto/$', 'homepage.views.contact', name='Contacto'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    (r'^login/$', 'django.contrib.auth.views.login',
                {'template_name': 'homepage/login.html', }),
    (r'^logout/$', 'homepage.views.logout_view', ),

)
