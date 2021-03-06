from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allstars.views.home', name='home'),
    # url(r'^allstars/', include('allstars.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^allstars/$', 'players.views.allstar_list', name='allstar_list'),
    url(r'^allstars/(?P<year>\d{4})/$', 'players.views.allstar_roster', name='allstar_roster')

)
