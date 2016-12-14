from django.conf.urls import url

from activist import views

urlpatterns = [
    url(r'^profile/(?P<input_profile_id>[0-9]+)/$', 
        views.activist_profile, name='activist_profile'),
    url(r'^profile/(?P<input_profile_id>[0-9]+)/groups$', 
        views.activist_profile_groups, name='activist_profile_groups'),
    url(r'^profile/(?P<input_profile_id>[0-9]+)/events$', 
        views.activist_profile_events, name='activist_profile_events'),
    url(r'^profile/(?P<input_profile_id>[0-9]+)/interests$', 
        views.activist_profile_interests, name='activist_profile_interests'),
    url(r'^group/(?P<input_group_id>[0-9]+)$', 
        views.activist_group, name='activist_group'),
    url(r'^group/(?P<input_group_id>[0-9]+)/events$', 
        views.activist_group_events, name='activist_group_events'),
    url(r'^event/(?P<input_group_id>[0-9]+)/create$', 
        views.create_activist_event, name='create_activist_event'),
    url(r'^event/(?P<input_group_id>[0-9]+)/delete$', 
        views.delete_activist_event, name='delete_activist_event'),
    url(r'^event/(?P<input_event_id>[0-9]+)$', 
        views.activist_event, name='activist_event'),
    url(r'^event/(?P<input_event_id>[0-9]+)/group$', 
        views.activist_event_group, name='activist_event_group'),
    url(r'^interest/(?P<input_interest_id>[0-9]+)$', 
        views.activist_interest, name='activist_interest'),
    url(r'^interest/(?P<input_interest_id>[0-9]+)/profiles$', 
        views.activist_interest_profiles, name='activist_interest_profiles'),

]
