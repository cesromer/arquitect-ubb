from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arquitect.views.home', name='home'),
    url(r'^$', 'homepage.views.single_img', name='Imagenes'),
)
