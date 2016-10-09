from django.conf.urls import url
import idea.views

urlpatterns = [
    url(r'^$', idea.views.list),
    url(r'^add/$', idea.views.add_idea, name='add_idea'),
    url(r'^add/(?P<banner_id>\d+)/$', idea.views.add_idea, name='add_idea'),
    url(r'^edit/(?P<idea_id>\d+)/$', idea.views.edit_idea, name='edit_idea'),
    url(r'^list/$', idea.views.list, name='idea_list'),
    url(r'^list/(?P<sort_or_state>\w+)/$', idea.views.list, name='idea_list'),
    url(r'^detail/(?P<idea_id>\d+)/$', idea.views.detail, name='idea_detail'),
    url(r'^detail/likes/(?P<idea_id>\d+)/$', idea.views.show_likes, name='show_likes'),
    url(r'^detail/(?P<idea_id>\d+)/remove_tag/(?P<tag_slug>[a-zA-Z0-9/\-_]+)/$',
        idea.views.remove_tag, name='remove_tag'),
    url(r'^vote/up/$', idea.views.up_vote, name='upvote_idea'),
    url(r'^challenge/(?P<banner_id>\d+)/$',
        idea.views.challenge_detail, name='challenge_detail'),
    url(r'^room/(?P<slug>.+)/$',
        idea.views.room_detail, name='room_detail'),
    url(r'challenge/list/$', idea.views.banner_list, name='banner_list'),
]
