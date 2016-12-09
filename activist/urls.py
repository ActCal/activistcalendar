from django.conf.urls import patterns, include, url
from activistcalendar import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^mission_and_vision/$', views.mission_and_vision, name='mission'),
	#url(r'^history/$', views.history, name='history'),
	url(r'^team/$', views.team, name='team'),
	url(r'^get_involved/$', views.get_involved, name='get_involved'),
	url(r'^contact_us/$', views.contact_us, name='contact_us'),
        url(r'^contact_submit/$', views.contact_submit, name='contact_submit'),
    url(r'^donate/$', views.donate, name='donate')

    # Examples:
    # url(r'^$', 'activist.views.home', name='home'),
    # url(r'^activist/', include('activist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
